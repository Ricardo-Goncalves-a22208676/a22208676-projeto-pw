from django.shortcuts import render, redirect
from .models import Autor, Artigo, Comentario, Classificacao
from .forms import autorForm, artigoForm, comentarioForm, classificacaoForm
from django.contrib.auth import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group

def autor_list_view(request):
    autores = Autor.objects.all()
    context = {'autores': autores}
    return render(request, 'artigos/autor_list.html', context)

def artigo_list_view(request):
    artigos = Artigo.objects.all()
    context = {'artigos': artigos}
    return render(request, 'artigos/artigo_list.html', context)

def autor_detail_view(request, username):
    autor = Autor.objects.get(user__username=username)
    artigos = Artigo.objects.filter(autor=autor)
    context = {'autor': autor, 'artigos': artigos}
    return render(request, 'artigos/autor_details.html', context)

def artigo_detail_view(request, artigo_titulo):
    artigo = Artigo.objects.get(titulo=artigo_titulo)
    comentarios = Comentario.objects.filter(artigo=artigo)
    classificacoes = Classificacao.objects.filter(artigo=artigo)
    classificacoes_sem_comentarios = [c for c in Classificacao.objects.filter(artigo=artigo) if not c.comentario_set.exists()]
    context = {'artigo': artigo, 'comentarios': comentarios, 'classificacoes': classificacoes, 'classificacoes_sem_comentarios': classificacoes_sem_comentarios}
    return render(request, 'artigos/artigo_details.html', context)

def admin_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        admin_group = Group.objects.get(name='administrador')
        if request.user.is_authenticated and admin_group in request.user.groups.all():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Acesso negado. Você não é um administrador.")
    return wrapped_view

@admin_required
def novo_autor_view(request):
    form = autorForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:index')

    context = {'form': form}
    return render(request, 'artigos/novo_autor.html', context)

@admin_required
def edita_autor_view(request, username):
    autor = Autor.objects.get(user__username=username)
    artigos = Artigo.objects.filter(autor=autor)

    if request.POST:
        form = autorForm(request.POST or None, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('artigos:autor_detail',autor.user.username)

    else:
        form = autorForm(instance=autor)

    context = {'form': form, 'autor':autor, 'artigos':artigos}
    return render(request, 'artigos/edita_autor.html', context)

@admin_required
def apaga_autor_view(request, username):
    autor = Autor.objects.get(user__username=username)
    autor.delete()
    return redirect('artigos:index')

@admin_required
def novo_artigo_view(request):

    form = artigoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:artigo_list')

    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)

@admin_required
def edita_artigo_view(request, artigo_titulo):
    artigo = Artigo.objects.get(titulo=artigo_titulo)
    autor = artigo.autor

    if request.POST:
        form = artigoForm(request.POST or None, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo_detail',artigo.titulo)
    else:
        form = artigoForm(instance=artigo)

    context = {'form': form, 'autor':autor, 'artigo':artigo}
    return render(request, 'artigos/edita_artigo.html', context)

@admin_required
def apaga_artigo_view(request, artigo_titulo):
    artigo = Artigo.objects.get(titulo=artigo_titulo)
    artigo.delete()
    return redirect('artigos:artigo_list')

@admin_required
def novo_comentario_view(request, artigo_titulo):
    artigo = Artigo.objects.get(titulo=artigo_titulo)
    autor = artigo.autor

    form = comentarioForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo_detail',artigo.titulo)

    else:
        form = comentarioForm(initial={'artigo': artigo,'autor':autor})

        context = {'form': form, 'autor':autor, 'artigo':artigo}
        return render(request, 'artigos/novo_comentario.html', context)

@admin_required
def edita_comentario_view(request, artigo_titulo, comentario_id):
    artigo = Artigo.objects.get(titulo=artigo_titulo)
    autor = artigo.autor
    comentario = Comentario.objects.get(id=comentario_id)

    if request.POST:
        form = comentarioForm(request.POST or None, request.FILES, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo_detail',artigo.titulo)
    else:
        form = comentarioForm(instance=comentario)

    context = {'form': form, 'autor':autor, 'artigo':artigo, 'comentario':comentario}
    return render(request, 'artigos/edita_comentario.html', context)

@admin_required
def apaga_comentario_view(request, artigo_titulo, comentario_id):
    artigo = Artigo.objects.get(titulo=artigo_titulo)
    comentario = Comentario.objects.get(id=comentario_id)
    comentario.delete()
    return redirect('artigos:artigo_detail',artigo.titulo)

@admin_required
def nova_classificacao_view(request, artigo_titulo):
    artigo = Artigo.objects.get(titulo=artigo_titulo)
    autor = artigo.autor

    form = classificacaoForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo_detail',artigo.titulo)

    else:
        form = classificacaoForm(initial={'artigo': artigo,'autor':autor})

        context = {'form': form, 'autor':autor, 'artigo':artigo}
        return render(request, 'artigos/novo_classificacao.html', context)

@admin_required
def edita_classificacao_view(request, artigo_titulo, classificacao_id):
    artigo = Artigo.objects.get(titulo=artigo_titulo)
    autor = artigo.autor
    classificacao = Classificacao.objects.get(id=classificacao_id)

    if request.POST:
        form = classificacaoForm(request.POST or None, request.FILES, instance=classificacao)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo_detail',artigo.titulo)
    else:
        form = classificacaoForm(instance=classificacao)

    context = {'form': form, 'autor':autor, 'artigo':artigo, 'classificacao':classificacao}
    return render(request, 'artigos/edita_classificacao.html', context)

@admin_required
def apaga_classificacao_view(request, artigo_titulo, classificacao_id):
    artigo = Artigo.objects.get(titulo=artigo_titulo)
    classificacao = Classificacao.objects.get(id=classificacao_id)
    classificacao.delete()
    return redirect('artigos:artigo_detail',artigo.titulo)

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('artigos:login')

    return render(request, 'artigos/registo.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('artigos:index')
        else:
            render(request, 'artigos/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'artigos/login.html')

def logout_view(request):
    logout(request)
    return redirect('artigos:login')
