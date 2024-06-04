from django import forms
from .models import AreaCientifica, Curso, Disciplina, Projeto, LinguagemProgramacao, Docente


class areaCientificaForm(forms.ModelForm):
  class Meta:
    model = AreaCientifica
    fields = '__all__'

class cursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = '__all__'

class disciplinaForm(forms.ModelForm):
  class Meta:
    model = Disciplina
    fields = '__all__'

class projetoForm(forms.ModelForm):
  class Meta:
    model = Projeto
    fields = '__all__'

class linguagemProgramacaoForm(forms.ModelForm):
  class Meta:
    model = LinguagemProgramacao
    fields = '__all__'

class docenteForm(forms.ModelForm):
  class Meta:
    model = Docente
    fields = '__all__'
