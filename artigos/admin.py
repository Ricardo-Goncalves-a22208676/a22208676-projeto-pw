from django.contrib import admin
from django.utils.html import format_html
from .models import Autor, Artigo, Comentario, Classificacao

class AutorAdmin(admin.ModelAdmin):
    list_display = ('username', 'mostrar_bio')
    search_fields = ('user__username', 'bio')
    ordering = ('user__username',)

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'

    def mostrar_bio(self, obj):
        return obj.bio
    mostrar_bio.short_description = 'Bio'

admin.site.register(Autor, AutorAdmin)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    search_fields = ('titulo', 'autor__user__username')
    ordering = ('data_publicacao',)

admin.site.register(Artigo, ArtigoAdmin)



class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('texto', 'autor', 'artigo', 'data_comentario')
    search_fields = ('texto', 'autor__user__username', 'artigo__titulo')
    ordering = ('data_comentario',)

admin.site.register(Comentario, ComentarioAdmin)

class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'autor', 'valor')
    search_fields = ('artigo__titulo', 'autor__user__username')
    ordering = ('artigo__titulo',)

admin.site.register(Classificacao, ClassificacaoAdmin)
