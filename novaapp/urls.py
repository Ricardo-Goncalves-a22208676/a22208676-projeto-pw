from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('interesses/', views.interesses, name='interesses'),

]