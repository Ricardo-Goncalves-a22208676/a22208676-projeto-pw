from django import forms
from .models import Autor, Artigo, Comentario, Classificacao

class autorForm(forms.ModelForm):
  class Meta:
    model = Autor
    fields = '__all__'

class artigoForm(forms.ModelForm):
  class Meta:
    model = Artigo
    fields = '__all__'

class comentarioForm(forms.ModelForm):
  class Meta:
    model = Comentario
    fields = '__all__'

class classificacaoForm(forms.ModelForm):
  class Meta:
    model = Classificacao
    fields = '__all__'