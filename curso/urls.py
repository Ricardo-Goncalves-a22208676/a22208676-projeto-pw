from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.curso_list_view, name='index'),
    path('nova_area', views.nova_areaCientifica_view, name="nova_area"),
    path('novo_curso', views.novo_curso_view, name="novo_curso"),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('<str:curso_nome>/', views.curso_detail_view, name='curso_detail'),
    path('<str:curso_nome>/edita_area', views.edita_areaCientifica_view, name="edita_area"),
    path('<str:curso_nome>/apaga_area', views.apaga_areaCientifica_view, name="apaga_area"),
    path('<str:curso_nome>/edita_curso', views.edita_curso_view, name="edita_curso"),
    path('<str:curso_nome>/apaga_curso', views.apaga_curso_view, name="apaga_curso"),
    path('<str:curso_nome>/nova_disciplina', views.nova_disciplina_view, name="nova_disciplina"),
    path('<str:curso_nome>/<str:disciplina_nome>/', views.disciplina_detail_view, name='disciplina_detail'),
    path('<str:curso_nome>/<str:disciplina_nome>/edita_disciplina', views.edita_disciplina_view, name='edita_disciplina'),
    path('<str:curso_nome>/<str:disciplina_nome>/apaga_disciplina', views.apaga_disciplina_view, name='apaga_disciplina'),
    path('<str:curso_nome>/<str:disciplina_nome>/nova_LinguagemProgramacao', views.nova_linguagemProgramacao_view, name='nova_LinguagemProgramacao'),
    path('<str:curso_nome>/<str:disciplina_nome>/novo_projeto/', views.novo_projeto_view, name='novo_projeto'),
    path('<str:curso_nome>/<str:disciplina_nome>/novo_docente', views.nova_docente_view, name='novo_docente'),
    path('<str:curso_nome>/<str:disciplina_nome>/projeto/', views.projeto_detail_view, name='projeto_detail'),
    path('<str:curso_nome>/<str:disciplina_nome>/projeto/edita', views.edita_projeto_view, name='edita_projeto'),
    path('<str:curso_nome>/<str:disciplina_nome>/projeto/apaga', views.apaga_projeto_view, name='apaga_projeto'),
    path('<str:curso_nome>/<str:disciplina_nome>/<str:linguagem_nome>/edita_LinguagemProgramacao', views.edita_linguagemProgramacao_view, name='edita_LinguagemProgramacao'),
    path('<str:curso_nome>/<str:disciplina_nome>/<str:linguagem_nome>/apaga_LinguagemProgramacao', views.apaga_linguagemProgramacao_view, name='apaga_LinguagemProgramacao'),
    path('<str:curso_nome>/<str:disciplina_nome>/<str:docente_nome>/edita_docente', views.edita_docente_view, name='edita_docente'),
    path('<str:curso_nome>/<str:disciplina_nome>/<str:docente_nome>/apaga_docente', views.apaga_docente_view, name='apaga_docente'),

]
