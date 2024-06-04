import requests
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta


def get_city_name(global_id_local):
    cidades_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cidades_url)
    response.raise_for_status()
    cidades_data = response.json()

    for cidade in cidades_data['data']:
        if cidade['globalIdLocal'] == global_id_local:
            return cidade['local']
    return 'Cidade Desconhecida'

def get_day_label(forecast_date):
    today = datetime.now().date()
    forecast_date = datetime.strptime(forecast_date, '%Y-%m-%d').date()

    dias_semana = {
    'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
    }

    if forecast_date == today:
        return "Hoje"
    elif forecast_date == today + timedelta(days=1):
        return "Amanhã"
    else:
        return dias_semana[forecast_date.strftime('%A')]

def get_wind_direction_angle(direction):
    directions = {
        'N': 0,
        'NE': 45,
        'E': 90,
        'SE': 135,
        'S': 180,
        'SW': 225,
        'W': 270,
        'NW': 315,
    }
    return directions.get(direction, 0)



def tempo_hoje_lisboa(request):

    previsao_url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    previsao_response = requests.get(previsao_url)
    previsao_response.raise_for_status()
    previsao_data = previsao_response.json()

    if not isinstance(previsao_data, dict) or 'data' not in previsao_data:
        raise ValueError("Resposta da API de previsão não é um JSON válido ou não contém 'data'")

    previsao_hoje = previsao_data['data'][0]
    weather_type = previsao_hoje['idWeatherType']
    wind_direction_angle = get_wind_direction_angle(previsao_hoje['predWindDir'])

    # Ajuste do nome do arquivo do ícone
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
        'data_label': get_day_label(previsao_hoje['forecastDate']),
        'icon_url': icon_url,
        'precipita_prob': previsao_hoje['precipitaProb'],
        'pred_wind_dir': previsao_hoje['predWindDir'],
        'wind_direction_angle': wind_direction_angle,
        'class_wind_speed': previsao_hoje['classWindSpeed'],
        'longitude': previsao_hoje['longitude'],
        'latitude': previsao_hoje['latitude'],
    }

    return render(request, 'meteo/tempo_hoje.html', context)


def tempo_5_dias(request):
    cidades_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cidades_response = requests.get(cidades_url)
    cidades_response.raise_for_status()
    cidades_data = cidades_response.json()

    global_id_local = request.GET.get('global_id_local')
    previsoes = []

    if global_id_local:
        previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_local}.json'

        previsao_response = requests.get(previsao_url)
        previsao_response.raise_for_status()
        previsao_data = previsao_response.json()

        if not isinstance(previsao_data, dict) or 'data' not in previsao_data:
            raise ValueError("Resposta da API de previsão não é um JSON válido ou não contém 'data'")

        for dia in previsao_data['data'][:5]:
            weather_type = dia['idWeatherType']
            wind_direction_angle = get_wind_direction_angle(dia['predWindDir'])

            current_hour = datetime.now().hour
            if 6 <= current_hour < 20:
                icon_name = f'w_ic_d_{weather_type:02}anim.svg'
            else:
                icon_name = f'w_ic_n_{weather_type:02}anim.svg'

            icon_url = f'/static/meteo/icons/{icon_name}'

            previsoes.append({
                'data_label': get_day_label(dia['forecastDate']),
                'temperatura_minima': dia['tMin'],
                'temperatura_maxima': dia['tMax'],
                'icon_url': icon_url,
                'precipita_prob': dia['precipitaProb'],
                'pred_wind_dir': dia['predWindDir'],
                'wind_direction_angle': wind_direction_angle,
                'class_wind_speed': dia['classWindSpeed'],
                'longitude': dia['longitude'],
                'latitude': dia['latitude'],
            })

        cidade_nome = get_city_name(int(global_id_local))
        msg='durante os próximos 5 dias'
    else:
        global_id_lisboa = 1110600
        previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_lisboa}.json'

        previsao_response = requests.get(previsao_url)
        previsao_response.raise_for_status()
        previsao_data = previsao_response.json()


        if not isinstance(previsao_data, dict) or 'data' not in previsao_data:
            raise ValueError("Resposta da API de previsão não é um JSON válido ou não contém 'data'")

        dia = previsao_data['data'][0]
        weather_type = dia['idWeatherType']
        wind_direction_angle = get_wind_direction_angle(dia['predWindDir'])

        current_hour = datetime.now().hour
        if 6 <= current_hour < 20:
            icon_name = f'w_ic_d_{weather_type:02}anim.svg'
        else:
            icon_name = f'w_ic_n_{weather_type:02}anim.svg'

        icon_url = f'/static/meteo/icons/{icon_name}'

        previsoes = [{
            'data_label': get_day_label(dia['forecastDate']),
            'temperatura_minima': dia['tMin'],
            'temperatura_maxima': dia['tMax'],
            'icon_url': icon_url,
            'precipita_prob': dia['precipitaProb'],
            'pred_wind_dir': dia['predWindDir'],
            'wind_direction_angle': wind_direction_angle,
            'class_wind_speed': dia['classWindSpeed'],
            'longitude': dia['longitude'],
            'latitude': dia['latitude'],
        }]

        cidade_nome = 'Lisboa'
        msg='hoje'

    context = {
        'cidades': cidades_data['data'],
        'cidade': cidade_nome,
        'msg':msg,
        'previsoes': previsoes,
        'global_id_local': global_id_local,
    }

    return render(request, 'meteo/previsao_5_dias.html', context)

def api_documentacao(request):
    return render(request, 'meteo/api_documentacao.html')

def api_lista_cidades(request):
    cidades_url = 'https://api.ipma.pt/open-data/distrits-islands.json'

    response = requests.get(cidades_url)
    response.raise_for_status()
    cidades_data = response.json()

    return JsonResponse(cidades_data)

def api_previsao_hoje(request, global_id_local):
    previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_local}.json'


    response = requests.get(previsao_url)
    response.raise_for_status()
    previsao_data = response.json()

    return JsonResponse(previsao_data)

def api_previsao_5_dias(request, global_id_local):
    previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_local}.json'


    response = requests.get(previsao_url)
    response.raise_for_status()
    previsao_data = response.json()

    return JsonResponse(previsao_data)

