from django.contrib import admin
from . import models

class MaquinaInline(admin.StackedInline):
    model = models.Maquina
    extra = 0
class ImpressoraInline(admin.StackedInline):
    model = models.Impressora
    extra = 0

class AmbienteAdmin(admin.ModelAdmin):
    inlines = [
        MaquinaInline,
        ImpressoraInline
    ]
    list_display = ('id', 'nome', 'nome_fantasia', 'estado', 'tipo')
    list_display_links = ('id', 'nome', 'nome_fantasia')
    list_per_page= 50
    search_fields =('nome', 'nome_fantasia', 'estado', 'tipo', 'cnpj', 'descricao')


admin.site.register(models.Ambiente, AmbienteAdmin),
admin.site.register(models.Maquina),
