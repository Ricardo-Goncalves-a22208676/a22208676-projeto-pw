from django.contrib import admin
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apresentacao', 'objetivos', 'competencias')
    search_fields = ('nome', 'apresentacao')

class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects', 'curso', 'area_cientifica')
    list_filter = ('ano', 'semestre', 'curso', 'area_cientifica')
    search_fields = ('nome', 'curso__nome', 'area_cientifica__nome')

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'descricao')
    search_fields = ('disciplina__nome', 'descricao')

class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    filter_horizontal = ('disciplinas',)
    search_fields = ('nome',)


admin.site.register(Curso, CursoAdmin)
admin.site.register(AreaCientifica, AreaCientificaAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(LinguagemProgramacao, LinguagemProgramacaoAdmin)
admin.site.register(Docente, DocenteAdmin)
