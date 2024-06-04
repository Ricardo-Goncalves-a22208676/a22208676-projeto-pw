from django.urls import path
from . import views

app_name = 'Festivais'

urlpatterns = [
    path('', views.festivais, name='festivais'),
    path('<int:festival_id>/', views.festival, name='festival'),
]
