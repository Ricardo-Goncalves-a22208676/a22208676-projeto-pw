# Generated by Django 4.0.6 on 2024-04-18 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0005_curso_area_cientifica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='area_cientifica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.areacientifica'),
        ),
    ]