from django.shortcuts import render,redirect
from .models import Curso, Disciplina, Projeto, LinguagemProgramacao, Docente, AreaCientifica
from .forms import areaCientificaForm, cursoForm, disciplinaForm, projetoForm, linguagemProgramacaoForm, docenteForm
from django.contrib.auth import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group

def curso_list_view(request):
    cursos = Curso.objects.all()

    context = {'cursos': cursos}
    return render(request, 'curso/curso_list.html', context)

def curso_detail_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplinas = Disciplina.objects.filter(curso=curso)
    projetos = Projeto.objects.filter(disciplina__in=disciplinas)
    context = {'curso': curso, 'disciplinas': disciplinas, 'projetos': projetos}
    return render(request, 'curso/curso_details.html', context)

def disciplina_detail_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    try:
        projeto = Projeto.objects.get(disciplina=disciplina)
        linguagens = LinguagemProgramacao.objects.filter(projetos=projeto)
    except Projeto.DoesNotExist:
        projeto = None
        linguagens = None
    docentes = Docente.objects.filter(disciplinas=disciplina)
    context = {'projeto': projeto, 'disciplina': disciplina, 'curso': curso, 'linguagens': linguagens, 'docentes': docentes}
    return render(request, 'curso/disciplina_details.html', context)

def projeto_detail_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    projeto = Projeto.objects.get(disciplina=disciplina)
    linguagens = LinguagemProgramacao.objects.filter(projetos=projeto)
    context = {'projeto': projeto, 'disciplina': disciplina, 'curso': curso, 'linguagens': linguagens}
    return render(request, 'curso/projeto_details.html', context)

def admin_required(*admin_group_names):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Acesso negado. Você não está autenticado.")

            user_groups = request.user.groups.all()
            admin_groups = Group.objects.filter(name__in=admin_group_names)

            if any(group in user_groups for group in admin_groups):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Acesso negado. Você não é um administrador.")

        return wrapped_view

    return decorator

@admin_required('administrador','curso')
def nova_areaCientifica_view(request):
    form = areaCientificaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form}
    return render(request, 'curso/nova_areaCientifica.html', context)

@admin_required('administrador','curso')
def edita_areaCientifica_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    areaCientifica = curso.area_cientifica

    if request.POST:
        form = areaCientificaForm(request.POST or None, request.FILES, instance=areaCientifica)
        if form.is_valid():
            form.save()
            return redirect('curso:index')

    else:
        form = areaCientificaForm(instance=areaCientifica)

    context = {'form': form,'curso': curso}
    return render(request, 'curso/editar_areaCientifica.html', context)

@admin_required('administrador')
def apaga_areaCientifica_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    areaCientifica = curso.area_cientifica
    areaCientifica.delete()
    return redirect('curso:index')

@admin_required('administrador','curso')
def novo_curso_view(request):
    form = cursoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form}
    return render(request, 'curso/novo_curso.html', context)

@admin_required('administrador','curso')
def edita_curso_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)

    if request.POST:
        form = cursoForm(request.POST or None, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso:curso_detail',curso.nome)

    else:
        form = cursoForm(instance=curso)

    context = {'form': form,'curso': curso}
    return render(request, 'curso/editar_curso.html', context)

@admin_required('administrador')
def apaga_curso_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    curso.delete()
    return redirect('curso:index')

@admin_required('administrador','curso')
def nova_disciplina_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    areaCientifica = curso.area_cientifica

    if request.method == 'POST':
        form = disciplinaForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('curso:curso_detail',curso.nome)

    else:
        form = disciplinaForm(initial={'curso': curso,'area_cientifica':areaCientifica})

    context = {'form': form,'curso': curso,'areaCientifica':areaCientifica}
    return render(request, 'curso/nova_disciplina.html', context)

@admin_required('administrador','curso')
def edita_disciplina_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)

    if request.POST:
        form = disciplinaForm(request.POST or None, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:disciplina_detail',curso.nome, disciplina.nome)

    else:
        form = disciplinaForm(instance=disciplina)

    context = {'form': form,'curso': curso,'disciplina': disciplina}
    return render(request, 'curso/editar_disciplina.html', context)

@admin_required('administrador')
def apaga_disciplina_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    disciplina.delete()
    return redirect('curso:curso_detail',curso.nome)

@admin_required('administrador','curso')
def novo_projeto_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)

    if request.method == 'POST':
        form = projetoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('curso:disciplina_detail',curso.nome, disciplina.nome)

    else:
        form = projetoForm(initial={'curso': curso,'disciplina':disciplina})

    context = {'form': form,'curso': curso}
    return render(request, 'curso/novo_projeto.html', context)

@admin_required('administrador','curso')
def edita_projeto_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    projeto = Projeto.objects.get(disciplina=disciplina)

    if request.POST:
        form = projetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('curso:projeto_detail',curso.nome, disciplina.nome)

    else:
        form = projetoForm(instance=projeto)

    context = {'form': form,'curso': curso,'disciplina': disciplina,'projeto':projeto}
    return render(request, 'curso/editar_projeto.html', context)

@admin_required('administrador')
def apaga_projeto_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    projeto = Projeto.objects.get(disciplina=disciplina)
    projeto.delete()
    return redirect('curso:disciplina_detail',curso.nome, disciplina.nome)

@admin_required('administrador','curso')
def nova_linguagemProgramacao_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    projetos = Projeto.objects.get(disciplina=disciplina)

    if request.method == 'POST':
        form = linguagemProgramacaoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('curso:projeto_detail',curso.nome, disciplina.nome)

    else:
        form = linguagemProgramacaoForm(initial={'projetos':projetos})

    context = {'form': form,'curso': curso,'disciplina':disciplina}
    return render(request, 'curso/novo_linguagemProgramacao.html', context)

@admin_required('administrador','curso')
def edita_linguagemProgramacao_view(request, curso_nome, disciplina_nome, linguagem_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    projeto = Projeto.objects.get(disciplina=disciplina)
    linguagem = LinguagemProgramacao.objects.get(nome=linguagem_nome)

    if request.POST:
        form = linguagemProgramacaoForm(request.POST or None, request.FILES, instance=linguagem)
        if form.is_valid():
            form.save()
            return redirect('curso:projeto_detail',curso.nome, disciplina.nome)

    else:
        form = linguagemProgramacaoForm(instance=linguagem)

    context = {'form': form,'curso': curso,'disciplina': disciplina,'projeto':projeto,'linguagem':linguagem}
    return render(request, 'curso/editar_linguagemProgramacao.html', context)

@admin_required('administrador')
def apaga_linguagemProgramacao_view(request, curso_nome, disciplina_nome, linguagem_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    linguagem = LinguagemProgramacao.objects.get(nome=linguagem_nome)
    linguagem.delete()
    return redirect('curso:projeto_detail',curso.nome, disciplina.nome)

@admin_required('administrador','curso')
def novo_docente_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)

    if request.method == 'POST':
        form = docenteForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('curso:disciplina_detail',curso.nome, disciplina.nome)

    else:
        form = docenteForm(initial={'disciplinas':disciplina})

    context = {'form': form,'curso': curso,'disciplinas':disciplina}
    return render(request, 'curso/novo_docente.html', context)

@admin_required('administrador','curso')
def edita_docente_view(request, curso_nome, disciplina_nome, docente_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    docente = Docente.objects.get(nome=docente_nome)

    if request.POST:
        form = docenteForm(request.POST or None, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('curso:disciplina_detail',curso.nome, disciplina.nome)

    else:
        form = docenteForm(instance=docente)

    context = {'form': form,'curso': curso,'disciplina': disciplina,'docente':docente}
    return render(request, 'curso/editar_docente.html', context)

@admin_required('administrador')
def apaga_docente_view(request, curso_nome, disciplina_nome, docente_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome, curso=curso)
    docente = Docente.objects.get(nome=docente_nome)
    docente.delete()
    return redirect('curso:disciplina_detail',curso.nome, disciplina.nome)

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('curso:login')

    return render(request, 'curso/registo.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('curso:index')
        else:
            render(request, 'curso/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'curso/login.html')

def logout_view(request):
    logout(request)
    return redirect('curso:login')