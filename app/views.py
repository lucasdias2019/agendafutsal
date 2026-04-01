from django.shortcuts import render
from django.views import View
from .models import Equipe 
from .models import Equipe, Agendamento

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class EquipesView(View):
    def get(self, request, *args, **kwargs):
        # Busca todas as equipes no banco (Equipe.objects.all)
        equipes = Equipe.objects.all() 
        return render(request, 'equipes.html', {'equipes': equipes})

class AgendamentosView(View):
    def get(self, request, *args, **kwargs):
        # Busca todos os agendamentos ordenados por data e hora
        agendamentos = Agendamento.objects.all().order_by('data', 'horario_inicio')
        return render(request, 'agendamentos.html', {'agendamentos': agendamentos})