from django.shortcuts import render
from .models import Trajeto

# Selecionando os dados da base de dados
def index(request):
    trajetos = Trajeto.objects.all()
    return render(request, 'trajetos/index.html', {
        'trajetos': trajetos
    })

def ver_trajeto(request, trajeto_id):
    trajeto = Trajeto.objects.get(id=trajeto_id)
    return render(request, 'trajetos/ver_trajeto.html', {
        'trajeto': trajeto
    })
