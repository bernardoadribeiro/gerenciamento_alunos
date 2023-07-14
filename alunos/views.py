from datetime import date
from django.shortcuts import render

from .models import Aluno


# Create your views here.

def index(request):
    """ View Index.
        Exibe o arquivo localizado em `/config/templates/index.html`
    """
    return render(request, 'index.html')


def alunos_cadastrados(request):
    """ View da tabelas contendo os Alunos Cadastrados.
    """
    alunos = Aluno.objects.all()

    for aluno in alunos:
        idade = (date.today() - aluno.data_nascimento).days // 365
        aluno.idade = idade

    context = {
        'alunos': alunos,
    }

    return render(request, 'alunos_cadastrados.html', context)


def cadastro_aluno(request):
    """ View do formulario de cadastro de aluno.
    """
    return render(request, 'cadastro_aluno.html')
