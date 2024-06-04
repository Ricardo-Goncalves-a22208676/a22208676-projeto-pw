from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='bandas/', null=True, blank=True)
    informacoes = models.TextField()
    biografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_foto_url(self):
        if self.foto and self.foto != '': # Check if foto field is not empty
            return self.foto.url
        else:
            return '/media/bandas/default_image.jpg'  # Path to your default image

class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)

    def __str__(self):
        return self.titulo

    def get_capa_url(self):
        if self.capa and hasattr(self.capa, 'url'):  # Verifica se a capa existe
            return self.capa.url
        else:
            return '/media/bandas/default_image.jpg'

class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    spotify_link = models.URLField(blank=True, null=True)
    letra = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.titulo
