# Generated by Django 4.0.6 on 2024-04-29 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0005_comentario_classificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='classificacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artigos.classificacao'),
        ),
    ]
