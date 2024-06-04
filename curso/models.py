from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=255)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()
    area_cientifica = models.ForeignKey('AreaCientifica', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()
    curricular_unit_code = models.CharField(max_length=20)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    descricao = models.TextField(null=True, blank=True)
    conceitos_aplicados = models.TextField(null=True, blank=True)
    tecnologias_usadas = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)
    video_demo = models.URLField(null=True, blank=True)
    github_repo = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome



class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=50)
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=255)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome

