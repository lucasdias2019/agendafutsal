from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Equipe")
    responsavel = models.CharField(max_length=100, verbose_name="Responsável")
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp (com DDD)")
    uniforme = models.CharField(max_length=50, verbose_name="Cor do Uniforme")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
        ('cancelado', 'Cancelado'),
        ('manutencao', 'Manutenção/Bloqueio'),
    ]

    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Equipe")
    data = models.DateField(verbose_name="Data do Amistoso")
    horario_inicio = models.TimeField(verbose_name="Horário de Início")
    horario_fim = models.TimeField(verbose_name="Horário de Término")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    justificativa = models.TextField(null=True, blank=True, verbose_name="Justificativa/Observação")
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        equipe_nome = self.equipe.nome if self.equipe else "Bloqueio Administrativo"
        return f"{equipe_nome} - {self.data} às {self.horario_inicio}"

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"