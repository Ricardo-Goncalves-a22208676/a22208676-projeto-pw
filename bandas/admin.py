from django.contrib import admin
from django.utils.html import format_html
from .models import Banda, Album, Musica

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'mostrar_foto', 'informacoes')
    search_fields = ('nome', 'informacoes')
    ordering = ('nome',)

    def mostrar_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 100px; height: 100px;" />', obj.foto.url)
        else:
            return format_html('<img src="/media/bandas/default_image.jpg" style="width: 100px; height: 100px;" />')
    mostrar_foto.short_description = 'Foto'


admin.site.register(Banda, BandaAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo','mostrar_capa', 'banda')
    search_fields = ('titulo',)
    ordering = ('titulo',)

    def mostrar_capa(self, obj):
        if obj.capa:
            return format_html('<img src="{}" style="width: 100px; height: 100px;" />', obj.capa.url)
        else:
            return format_html('<img src="/media/bandas/default_image.jpg" style="width: 100px; height: 100px;" />')
    mostrar_capa.short_description = 'Capa'

admin.site.register(Album, AlbumAdmin)

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'mostrar_spotify_link')
    search_fields = ('titulo',)
    ordering = ('titulo',)

    def mostrar_spotify_link(self, obj):
        if obj.spotify_link:
            return format_html('<a href="{}" target="_blank">{}</a>', obj.spotify_link, obj.spotify_link)
        else:
            return ''
    mostrar_spotify_link.short_description = 'Spotify Link'


admin.site.register(Musica, MusicaAdmin)
