from django.db import models

class Pessoa(models.Model):
    GENDER_CHOICES = (
        ('ND', 'Não definido'),
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    data_nascimento = models.DateField(null=True)
    cpf = models.CharField(max_length=14, null=True)
    email = models.CharField(max_length=100, null=True)
    sexo = models.CharField(max_length=2, choices=GENDER_CHOICES, default='ND')

    def __str__(self):
        return f"{self.nome} (ID={self.id})"

    '''def detalhar(self):
        result = Endereco.objects.filter(pessoa__id=self.id)
        print(result)
        if(result):
           return result[0]'''

