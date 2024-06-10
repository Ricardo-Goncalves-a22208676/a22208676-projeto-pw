from django.shortcuts import render,redirect
import requests
from datetime import datetime
from django.contrib.auth import models, authenticate, login, logout

def index(request):

    previsao_url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    previsao_response = requests.get(previsao_url)
    previsao_response.raise_for_status()
    previsao_data = previsao_response.json()

    if not isinstance(previsao_data, dict) or 'data' not in previsao_data:
        raise ValueError("Resposta da API de previsão não é um JSON válido ou não contém 'data'")

    previsao_hoje = previsao_data['data'][0]
    weather_type = previsao_hoje['idWeatherType']

    current_hour = datetime.now().hour
    if 6 <= current_hour < 20:
        icon_name = f'w_ic_d_{weather_type:02}anim.svg'
    else:
        icon_name = f'w_ic_n_{weather_type:02}anim.svg'

    icon_url = f'/static/meteo/icons/{icon_name}'

    context = {
        'cidade': 'Lisboa',
        'temperatura_minima': previsao_hoje['tMin'],
        'temperatura_maxima': previsao_hoje['tMax'],
        'icon_url': icon_url,
    }

    return render(request, 'portfolio/index.html', context)

def about_me(request):
    return render(request, 'portfolio/about_me.html')

def about_site(request):
    return render(request, 'portfolio/about_site.html')

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('portfolio:login')

    return render(request, 'portfolio/registo.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('portfolio:index')
        else:
            render(request, 'portfolio/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)
    return redirect('portfolio:login')