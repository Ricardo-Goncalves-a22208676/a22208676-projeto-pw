# Generated by Django 4.0.6 on 2024-05-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0004_musica_biografia_musica_letra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musica',
            name='biografia',
        ),
        migrations.AddField(
            model_name='banda',
            name='biografia',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
