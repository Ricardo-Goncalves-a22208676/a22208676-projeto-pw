from django.contrib import admin
from .models import Festival, Localizacao, Banda

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao')
    search_fields = ('nome',)
    list_filter = ('localizacao',)

admin.site.register(Banda, BandaAdmin)
admin.site.register(Localizacao, LocalizacaoAdmin)
admin.site.register(Festival, FestivalAdmin)
