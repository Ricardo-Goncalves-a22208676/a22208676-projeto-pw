#import os
#import django
from django.db.models import Count


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
#django.setup()


from curso.models import Curso, Disciplina, AreaCientifica

def explore_database():
    try:

        print("1. Nome das disciplinas, ordenadas alfabeticamente:")
        disciplinas_ordenadas = Disciplina.objects.order_by('nome')
        for disciplina in disciplinas_ordenadas:
            print(disciplina.nome)


        print("\n2. Nome dos cursos, ordenados alfabeticamente:")
        cursos_ordenados = Curso.objects.order_by('nome')
        for curso in cursos_ordenados:
            print(curso.nome)


        print("\n3. Todas as áreas científicas:")
        areas_cientificas = AreaCientifica.objects.all()
        for area in areas_cientificas:
            print(area.nome)


        print("\n4. Nome das disciplinas e o nome do curso a que pertencem:")
        disciplinas_com_curso = Disciplina.objects.select_related('curso')
        for disciplina in disciplinas_com_curso:
            print(f"Disciplina: {disciplina.nome}, Curso: {disciplina.curso.nome}")


        print("\n5. Nome das disciplinas e a área científica a que pertencem:")
        disciplinas_com_area = Disciplina.objects.select_related('area_cientifica')
        for disciplina in disciplinas_com_area:
            print(f"Disciplina: {disciplina.nome}, Área Científica: {disciplina.area_cientifica.nome}")


        print("\n6. Disciplinas com mais de 6 ECTS:")
        disciplinas_mais_ects = Disciplina.objects.filter(ects__gt=6)
        for disciplina in disciplinas_mais_ects:
            print(disciplina.nome)


        print("\n7. Áreas científicas com disciplinas:")
        areas_com_disciplinas = AreaCientifica.objects.filter(disciplina__isnull=False).distinct()
        for area in areas_com_disciplinas:
            print(area.nome)

        print("\n8. Número de disciplinas por curso:")
        disciplinas_por_curso = Curso.objects.annotate(num_disciplinas=Count('disciplina'))
        for curso in disciplinas_por_curso:
            print(f"Curso: {curso.nome}, Número de disciplinas: {curso.num_disciplinas}")




    except Exception as e:
        print(f"Ocorreu um erro durante a exploração da base de dados: {e}")

# Call the function to explore the database
#explore_database()
