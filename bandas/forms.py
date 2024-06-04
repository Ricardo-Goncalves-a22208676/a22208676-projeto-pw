from django import forms
from .models import Banda, Album, Musica


class bandaForm(forms.ModelForm):
  class Meta:
    model = Banda
    fields = '__all__'

    widgets = {
      'nome': forms.TextInput(attrs={
          'placeholder':'Nome completo da banda',
      })
    }

    labels = {
      'nome': 'Nome da Banda',
    }

    help_texts = {
            'nome': 'Insira o nome da banda.',
            'foto': 'Carregue uma foto que represente a banda.',
            'informacoes': 'Inclua informações importantes sobre a banda.',
            'biografia': 'Insira uma breve biografia de 4-5 linhas.',
        }

class albumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'

    widgets = {
      'titulo': forms.TextInput(attrs={
          'placeholder':'Título do álbum',
      })
    }

    labels = {
      'titulo': 'Título do Álbum',
    }

    help_texts = {
            'titulo': 'Insira o título do álbum.',
            'banda': 'Escolha a banda à qual este álbum pertence.',
            'capa': 'Carregue uma imagem que representa a capa do álbum.',
        }

class musicaForm(forms.ModelForm):
  class Meta:
    model = Musica
    fields = '__all__'

    widgets = {
      'titulo': forms.TextInput(attrs={
          'placeholder':'Título da música',
      })
    }

    labels = {
      'titulo': 'Título da Música',
    }

    help_texts = {
            'titulo': 'Insira o título da música.',
            'album': 'Escolha o álbum ao qual esta música pertence.',
            'spotify_link': 'Se disponível, forneça o link do Spotify para esta música.',
            'letra': 'Insira a letra completa da música, se houver.',
            'biografia': 'Forneça uma breve biografia relacionada a esta música.',
        }
