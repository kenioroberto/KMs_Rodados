from django.db import models
from django.utils import timezone


class Motivo(models.Model):
        nome_motivo = models.CharField(max_length=255, verbose_name='Motivo da Visita')
        
        def __str__(self):
            return self.nome_motivo

class Trajeto(models.Model):
    saida =models.CharField(max_length=255, verbose_name='Saída')
    destino =models.CharField(max_length=255, verbose_name='Destino')
    kilometragem =models.FloatField(verbose_name= 'Kms')
    data_visita= models.DateTimeField(verbose_name='Data da visita')
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    motivo = models.ForeignKey(Motivo, on_delete=models.DO_NOTHING)
    
    def __str__(self):
            return self.saida