from django.contrib import admin
from . models import Trajeto, Motivo

class TrajetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'saida', 'destino', 'kilometragem', 'motivo', 'data_visita')
    list_display_links = ('id', 'saida', 'destino')
    list_per_page= 50
    search_fields = ('saida', 'destino', 'kilometragem', 'motivo', 'data_visita')

admin.site.register(Motivo)
admin.site.register(Trajeto, TrajetoAdmin)


# Register your models here.
