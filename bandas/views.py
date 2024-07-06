from django.shortcuts import render, redirect
from .models import Banda, Album, Musica
from .forms import bandaForm, albumForm, musicaForm
from django.contrib.auth import models
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from django.http import JsonResponse




def band_list_view(request):
    bandas = Banda.objects.all()
    try:
        abbey_road_album = Album.objects.get(titulo="Abbey Road")
        come_together_song = Musica.objects.get(album=abbey_road_album, titulo="Come Together")
    except Album.DoesNotExist:
        abbey_road_album = None
        come_together_song = None
    except Musica.DoesNotExist:
        come_together_song = None

    context = {
        'bandas': bandas,
        'abbey_road_album': abbey_road_album,
        'come_together_song': come_together_song,
    }
    return render(request, 'bandas/list_of_bands.html', context)


def band_detail_view(request, band_name):
    banda = Banda.objects.get(nome=band_name)
    albuns = Album.objects.filter(banda=banda).order_by('-titulo')
    total_musicas = Musica.objects.filter(album__banda=banda).count()

    context = {
        'banda': banda,
        'albuns': albuns,
        'total_musicas': total_musicas
    }
    return render(request, 'bandas/band_details.html', context)

def album_detail_view(request, album_title):
    album = Album.objects.get(titulo=album_title)
    musicas = Musica.objects.filter(album=album)
    context = {'album': album, 'musicas': musicas}
    return render(request, 'bandas/album_details.html', context)

def song_detail_view(request, song_title):
    musica = Musica.objects.get(titulo=song_title)
    context = {'musica': musica}
    return render(request, 'bandas/song_details.html', context)

def htmlAndCss_view(request):
    return render(request, 'bandas/html5-css.html')

def bandas_list_json(request):
    bandas = Banda.objects.all()
    bandas_list = [{'nome': banda.nome} for banda in bandas]
    return JsonResponse(bandas_list, safe=False)

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


@admin_required('administrador','banda')
def nova_banda_view(request):
    form = bandaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:index')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

@admin_required('administrador','banda')
def edita_banda_view(request, band_name):
    banda = Banda.objects.get(nome=band_name)

    if request.POST:
        form = bandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:band_detail', banda.nome)

    else:
        form = bandaForm(instance=banda)

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/editar_banda.html', context)

@admin_required('administrador')
def apaga_banda_view(request, band_name):
    banda = Banda.objects.get(nome=band_name)
    banda.delete()
    return redirect('bandas:index')

@admin_required('administrador','banda')
def novo_album_view(request, band_name):
    banda = Banda.objects.get(nome=band_name)

    if request.method == 'POST':
        form = albumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.banda = banda
            album.save()
            return redirect('bandas:band_detail', banda.nome)
    else:
        form = albumForm(initial={'banda': banda})

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/novo_album.html', context)

@admin_required('administrador','banda')
def edita_album_view(request, album_title):
    album = Album.objects.get(titulo=album_title)
    banda = album.banda

    if request.method == 'POST':
        form = albumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:album_detail', album.titulo)
    else:
        form = albumForm(instance=album)

    context = {'form': form, 'album': album, 'banda': banda}
    return render(request, 'bandas/editar_album.html', context)

@admin_required('administrador')
def apaga_album_view(request, album_title):
    album = Album.objects.get(titulo=album_title)
    banda = album.banda
    album.delete()
    return redirect('bandas:band_detail', banda.nome)

@admin_required('administrador','banda')
def nova_musica_view(request, album_title):
    album = Album.objects.get(titulo=album_title)

    if request.method == 'POST':
        form = musicaForm(request.POST, request.FILES)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.album = album
            musica.save()
            return redirect('bandas:album_detail', album.titulo)
    else:
        form = musicaForm(initial={'album': album})

    context = {'form': form, 'album': album}
    return render(request, 'bandas/nova_musica.html', context)

@admin_required('administrador','banda')
def edita_musica_view(request, song_title):
    musica = Musica.objects.get(titulo=song_title)
    album = musica.album

    if request.method == 'POST':
        form = musicaForm(request.POST, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:song_detail', musica.titulo)
    else:
        form = musicaForm(instance=musica)

    context = {'form': form, 'album': album, 'musica': musica}
    return render(request, 'bandas/editar_musica.html', context)

@admin_required('administrador')
def apaga_musica_view(request, song_title):
    musica = Musica.objects.get(titulo=song_title)
    album = musica.album
    musica.delete()
    return redirect('bandas:album_detail', album.titulo)


def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('bandas:login')

    return render(request, 'bandas/registo.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('bandas:index')
        else:
            render(request, 'bandas/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'bandas/login.html')

def logout_view(request):
    logout(request)
    return redirect('bandas:login')
