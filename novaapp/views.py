from django.shortcuts import render
from datetime import datetime


def index(request):
    return render(request, 'novaapp/index.html',{
        'data': datetime.today()
        })
def sobre(request):
    return render(request, 'novaapp/sobre.html',{
        'data': datetime.today()
        })
def interesses(request):
    return render(request, 'novaapp/interesses.html',{
        'data': datetime.today()
        })
