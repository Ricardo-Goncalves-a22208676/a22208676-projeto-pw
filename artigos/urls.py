from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.autor_list_view, name='index'),
    path('autor/<str:username>', views.autor_detail_view, name='autor_detail'),
    path('artigo/<str:artigo_titulo>', views.artigo_detail_view, name='artigo_detail'),
    path('artigos/', views.artigo_list_view, name='artigo_list'),
    path('novo_autor', views.novo_autor_view, name="novo_autor"),
    path('autor/<str:username>/edita', views.edita_autor_view, name="edita_autor"),
    path('autor/<str:username>/apaga', views.apaga_autor_view, name="apaga_autor"),
    path('artigos/novo_artigo', views.novo_artigo_view, name='novo_artigo'),
    path('artigo/<str:artigo_titulo>/edita', views.edita_artigo_view, name='edita_artigo'),
    path('artigo/<str:artigo_titulo>/apaga', views.apaga_artigo_view, name='apaga_artigo'),
    path('artigo/<str:artigo_titulo>/novo_comentario', views.novo_comentario_view, name='novo_comentario'),
    path('artigo/<str:artigo_titulo>/nova_classificacao', views.nova_classificacao_view, name='nova_classificacao'),
    path('artigo/<str:artigo_titulo>/<int:comentario_id>/edita_comentario', views.edita_comentario_view, name='edita_comentario'),
    path('artigo/<str:artigo_titulo>/<int:comentario_id>/apaga_comentario', views.apaga_comentario_view, name='apaga_comentario'),
    path('artigo/<str:artigo_titulo>/<int:classificacao_id>/edita_classificacao', views.edita_classificacao_view, name='edita_classificacao'),
    path('artigo/<str:artigo_titulo>/<int:classificacao_id>/apaga_classificacao', views.apaga_classificacao_view, name='apaga_classificacao'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout")
]
