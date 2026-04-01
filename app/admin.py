from django.contrib import admin
from .models import Equipe, Agendamento

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'responsavel', 'whatsapp')
    search_fields = ('nome', 'responsavel')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('get_equipe', 'data', 'horario_inicio', 'status')
    list_filter = ('status', 'data')
    date_hierarchy = 'data'
    
    def get_equipe(self, obj):
        return obj.equipe.nome if obj.equipe else "BLOQUEIO/MANUTENÇÃO"
    get_equipe.short_description = 'Equipe/Evento'