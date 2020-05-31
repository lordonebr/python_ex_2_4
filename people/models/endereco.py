from django.db import models
from .pessoa import Pessoa

class Endereco(models.Model):
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=200)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100, null=True)
    cep = models.CharField(max_length=9, null=True)
    municipio = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=2, choices=UF_CHOICES, default='MG')

    """
    LINHA DE COMENTÁRIO
    """
    def __str__(self):
        detalhe+= f"""{self.logradouro}, {self.numero}.
            Bairro {self.bairro}. CEP: {self.cep}
        """

        return detalhe