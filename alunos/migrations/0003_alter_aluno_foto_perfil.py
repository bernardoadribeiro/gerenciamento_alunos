# Generated by Django 4.2.3 on 2023-07-23 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_alter_aluno_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='foto_perfil',
            field=models.CharField(max_length=512),
        ),
    ]
