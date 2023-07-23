from django.db import models

# from stdimage.models import StdImageField


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    # foto_perfil = StdImageField('Foto do Aluno', upload_to='alunos',
    #                             variations={'thumb': (200, 200)})
    foto_perfil = models.CharField(max_length=512)
    cpf = models.CharField(max_length=11)  # Desconsidera pontuacao
    rg = models.CharField(max_length=10)   # Desconsidera pontuacao
    curso = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_ingresso = models.DateField()

    def __str__(self) -> str:
        return str(self.nome)
