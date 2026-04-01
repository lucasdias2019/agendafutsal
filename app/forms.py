from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        # Selecionamos apenas os campos que o usuário deve preencher
        fields = ['equipe', 'data', 'horario_inicio', 'horario_fim']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'horario_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'horario_fim': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'equipe': forms.Select(attrs={'class': 'form-control'}),
        }