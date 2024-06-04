from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Artigo(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    classificacao_media = models.FloatField(default=0)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
    classificacao = models.ForeignKey('Classificacao', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.texto[:50]

class Classificacao(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    MUITO_MAU = '⭐'
    MAU = '⭐⭐'
    INDIFERENTE = '⭐⭐⭐'
    BOM = '⭐⭐⭐⭐'
    MUITO_BOM = '⭐⭐⭐⭐⭐'

    RATINGS_CHOICES = [
        (MUITO_MAU, '⭐'),
        (MAU, '⭐⭐'),
        (INDIFERENTE, '⭐⭐⭐'),
        (BOM, '⭐⭐⭐⭐'),
        (MUITO_BOM, '⭐⭐⭐⭐⭐'),
    ]
    valor = models.CharField(max_length=10, choices=RATINGS_CHOICES, default=MUITO_MAU, blank=True, null=True)

    def __str__(self):
        return f"{self.artigo.titulo} - {self.autor.user.username}: {self.valor}"

