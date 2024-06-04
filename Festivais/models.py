from django.db import models

class Localizacao(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=200)
    festivais = models.ManyToManyField('Festival', related_name='bandas')

    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=200)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='festivais/', null=True, blank=True)

    def __str__(self):
        return self.nome

