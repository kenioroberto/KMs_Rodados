
from codecs import backslashreplace_errors
from operator import truediv
from django.db import models
from django.conf import settings
import os


class Ambiente(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome do Cliente')
    nome_fantasia = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255, blank=True)
    cnpj = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=75, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    estado = models.CharField(
        max_length=2,
        default='DF',
        choices=(
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
    )
    descricao = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Varejo'),
            ('S', 'Atacado'),
            ('F', 'Food'),
        )
    )
    
    def __str__(self):
        return self.nome


class Maquina(models.Model):
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    processador = models.CharField(max_length=50, blank=True, null=True)
    memoria = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, verbose_name='Endereço de IP')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('T', 'Terminal'),
            ('S', 'Servidor'),
           
        )
    )

    def __str__(self):
        return self.nome or self.ambiente.nome

    class Meta:
        verbose_name = 'Maquina'
        verbose_name_plural = 'Maquinas'


class Impressora(models.Model):
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nome da impressora no windows')
    marca = models.CharField(
        default='E',
        max_length=1,
        choices=(
            ('E', 'Epson'),
            ('B', 'Bematech'),
            ('G', 'Elgin'),
            ('D', 'Daruma'),
            ('O', 'Outros'),
            ('Z', 'Zebra'),
           
        )
    )
    modelo = models.CharField(max_length=70, blank=True, null=True)
    setor = models.CharField(
        default='E',
        max_length=1,
        choices=(
            ('E', 'Caixa'),
            ('B', 'Cozinha'),
            ('G', 'Bar'),
            ('D', 'Cafeteria'),
            ('O', 'Salão'),
            ('P', 'Parrila'),
            ('A', 'Administrativo'),
           
        )
    )
    ip = models.CharField(max_length=20, blank=True, verbose_name='Endereço de IP')
    descricao = models.CharField(max_length=255, blank=True, null=True)
      
    

    def __str__(self):
        return self.nome or self.ambiente.nome

    class Meta:
        verbose_name = 'Impressora'
        verbose_name_plural = 'Impressoras'