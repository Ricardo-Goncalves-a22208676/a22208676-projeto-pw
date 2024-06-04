# meteo/urls.py
from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('tempo_hoje_lisboa/', views.tempo_hoje_lisboa, name='tempo_hoje_lisboa'),
    path('', views.tempo_5_dias, name='index'),
    path('api/documentacao/', views.api_documentacao, name='api_documentacao'),
    path('api/lista_cidades/', views.api_lista_cidades, name='api_lista_cidades'),
    path('api/previsao_hoje/<int:global_id_local>/', views.api_previsao_hoje, name='api_previsao_hoje'),
    path('api/previsao_5_dias/<int:global_id_local>/', views.api_previsao_5_dias, name='api_previsao_5_dias'),

]

