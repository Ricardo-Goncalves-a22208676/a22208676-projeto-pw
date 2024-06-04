from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.band_list_view, name='index'),
    path('htmlAndCss/', views.htmlAndCss_view, name='htmlAndCss'),
    path('banda/<str:band_name>', views.band_detail_view, name='band_detail'),
    path('album/<str:album_title>', views.album_detail_view, name='album_detail'),
    path('musica/<str:song_title>', views.song_detail_view, name='song_detail'),
    path('nova_banda', views.nova_banda_view, name="nova_banda"),
    path('banda/<str:band_name>/edita', views.edita_banda_view, name="edita_banda"),
    path('banda/<str:band_name>/apaga', views.apaga_banda_view, name="apaga_banda"),
    path('banda/<str:band_name>/novo_album', views.novo_album_view, name="novo_album"),
    path('album/<str:album_title>/edita', views.edita_album_view, name='edita_album'),
    path('album/<str:album_title>/apaga', views.apaga_album_view, name='apaga_album'),
    path('album/<str:album_title>/nova_musica', views.nova_musica_view, name='nova_musica'),
    path('musica/<str:song_title>/edita', views.edita_musica_view, name='edita_musica'),
    path('musica/<str:song_title>/apaga', views.apaga_musica_view, name='apaga_musica'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout")
]
