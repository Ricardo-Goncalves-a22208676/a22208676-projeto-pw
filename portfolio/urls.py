from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('About_Me/', views.about_me, name='about_me'),
    path('About_My_Site/', views.about_site, name='about_site'),
    path('about_automation/', views.about_automation, name='about_automation'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
