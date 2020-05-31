from django.db import models
from .pessoa import Pessoa

class Trabalho(models.Model):

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    temEmprego = models.BooleanField(default=False)
    empresa = models.CharField(max_length=200, null=True)
    cargo = models.CharField(max_length=200, null=True)

