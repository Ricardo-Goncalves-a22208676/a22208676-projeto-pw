from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('sobre/', views.index_view1, name='sobre'),
    path('interesses/', views.index_view2, name='interesses'),


]