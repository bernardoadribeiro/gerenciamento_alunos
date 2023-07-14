# Generated by Django 4.2.3 on 2023-07-14 20:55

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='foto_perfil',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='alunos', variations={'thumb': (200, 200)}, verbose_name='Foto do Aluno'),
        ),
    ]