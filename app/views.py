from django.shortcuts import render
from django.views import View
from .models import Equipe 
from .models import Equipe, Agendamento
from django.shortcuts import redirect
from .forms import AgendamentoForm

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

class SolicitarAgendamentoView(View):
    def get(self, request):
        form = AgendamentoForm()
        return render(request, 'solicitar_agendamento.html', {'form': form})

    def post(self, request):
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save() # Salva como 'pendente' por padrão (definido na model)
            return redirect('agendamentos')
        return render(request, 'solicitar_agendamento.html', {'form': form})