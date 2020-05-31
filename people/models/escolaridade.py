from django.db import models
from django.core.validators import MinValueValidator
from .pessoa import Pessoa

class Escolaridade(models.Model):
    PROGRESS_CHOICES = (
        ('N', 'Não cursado'),
        ('I', 'Incompleto'),
        ('C', 'Completo'),
    )

    SCHOLARITY_CHOICES = (
        ('F', 'Ensino Fundamental'),
        ('M', 'Ensino Médio'),
        ('G', 'Graduação'),
        ('P', 'Pós-graduação'),
    )

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    progresso = models.CharField(max_length=1, choices=PROGRESS_CHOICES, default='N')
    nivel = models.CharField(max_length=1, choices=SCHOLARITY_CHOICES, default='F')
    instituicao = models.CharField(max_length=200)
    anoFinal = models.IntegerField(default=2020, null=True, validators = [MinValueValidator(1900)])

