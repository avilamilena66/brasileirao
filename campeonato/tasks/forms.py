from django import forms
from django.contrib.auth import get_user_model
from .models import Insulina
from .models import Glicose
from .models import Meal
from .models import AtividadeFisica

class UserUpdateForm(forms.ModelForm):
    class Meta:
        fields = ('first_name', 'username', 'password')
        model = get_user_model()

class InsulinaForm(forms.ModelForm):
    class Meta:
        model = Insulina
        fields = ['data', 'horario', 'refeicao', 'antes_depois_refeicao', 'tipo_insulina', 'quantidade']
        help_texts = {
            'data': 'Informe a data da aplicação de insulina',
            'horario': 'Informe o horário da aplicação de insulina',
        }

class GlicoseForm(forms.ModelForm):
    class Meta:
        model = Glicose
        fields = ['sugar_level', 'data', 'horario', 'refeicao', 'antes_depois_refeicao']
        help_texts = {
            'sugar_level': 'Informe o nível glicêmico',
            'data': 'Informe a data da medição glicêmica',
        }

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['data', 'horario', 'refeicao', 'quantidade']
        help_texts = {
            'data': 'Informe a data da medição glicêmica',
        }

class AtividadeFisicaForm(forms.ModelForm):
    class Meta:
        model = AtividadeFisica
        fields = ['data', 'horario', 'tipo_atividade', 'duracao', 'intensidade']
        help_texts = {
            'data': 'Informe a data da atividade física',
            'horario': 'Informe o horário da atividade física',
        }