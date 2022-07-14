from django.shortcuts import render
from .models import Ambiente
from django.views.generic.list import ListView

def index(request):
    ambiente = Ambiente.objects.all()
    return render(request, 'ambiente/index.html', {
        'ambiente': ambiente
    })

def ver_ambiente(request, ambiente_id):
    ambiente = Ambiente.objects.get(id=ambiente_id)
    return render(request, 'ambiente/ver_ambiente.html', {
        'ambiente': ambiente
    })
