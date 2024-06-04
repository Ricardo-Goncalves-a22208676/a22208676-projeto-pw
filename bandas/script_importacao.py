import json
import os
from bandas.models import Banda, Album, Musica

def importar_bandas(file_path):
    with open(file_path, 'r') as file:
        bandas_data = json.load(file)
        for banda_info in bandas_data:
            banda, created = Banda.objects.get_or_create(
                nome=banda_info['nome'],
                defaults={'informacoes': f"Nacionalidade: {banda_info['nacionalidade']}, Ano de criação: {banda_info['ano_criacao']}"}
            )

def importar_albuns(file_path):
    with open(file_path, 'r') as file:
        albuns_data = json.load(file)
        for album_info in albuns_data:
            banda = Banda.objects.get(nome=album_info['banda'])
            album, created = Album.objects.get_or_create(
                banda=banda,
                titulo=album_info['titulo']
            )
            for musica_info in album_info['musicas']:
                Musica.objects.get_or_create(
                    album=album,
                    titulo=musica_info['titulo'],
                    defaults={'spotify_link': ''}  # Supondo que não temos o link do Spotify
                )

def importar_curso(bandas_json, albuns_json):
    importar_bandas(bandas_json)
    importar_albuns(albuns_json)

# Obtém o caminho absoluto do arquivo bandas.json
bandas_json_path = os.path.join(os.path.dirname(__file__), 'bandas.json')

# Obtém o caminho absoluto do arquivo albuns.json
albuns_json_path = os.path.join(os.path.dirname(__file__), 'albuns.json')

# Chama a função importar_curso com os caminhos absolutos dos arquivos
importar_curso(bandas_json_path, albuns_json_path)
