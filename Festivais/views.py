from django.shortcuts import render
from .models import Festival, Localizacao, Banda

def festivais(request):
    localizacoes = Localizacao.objects.all()
    festivais = Festival.objects.all()
    return render(request, 'Festivais/festivais.html', {'localizacoes': localizacoes, 'festivais': festivais})


def festival(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    bandas = festival.bandas.all()
    return render(request, 'Festivais/festival.html', {'festival': festival, 'bandas': bandas})

