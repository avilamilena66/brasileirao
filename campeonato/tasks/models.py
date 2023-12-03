# models.py
from django.db import models
from django.contrib.auth.models import User

class Insulina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    refeicao = models.CharField(max_length=20)
    antes_depois_refeicao = models.CharField(max_length=20)
    tipo_insulina = models.CharField(max_length=50)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.data} {self.horario}'


class Glicose(models.Model):
    '''
    Índice Glicêmico: sugar_level
    Data: date
    Horário: time
    Refeição: refeicao
    Antes ou depois: antes_depois_refeicao 

    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sugar_level = models.IntegerField()
    data = models.DateField()
    horario = models.TimeField()
    refeicao = models.CharField(max_length=20)
    antes_depois_refeicao = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username} - {self.data} {self.horario}'
    
class Meal(models.Model):
    '''
    Índice Glicêmico: sugar_level
    Data: date
    Horário: time
    Refeição: refeicao
    Antes ou depois: antes_depois_refeicao 

    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    refeicao = models.CharField(max_length=20)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.data} {self.horario}'
    
class AtividadeFisica(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    tipo_atividade = models.CharField(max_length=255)
    duracao = models.IntegerField()
    intensidade = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.tipo_atividade} - {self.data}"