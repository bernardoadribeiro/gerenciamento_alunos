from django.shortcuts import render


# Create your views here.

def index(request):
    """ View Index.
        Exibe o arquivo localizado em `/config/templates/index.html`
    """
    return render(request, 'index.html')


def alunos_cadastrados(request):
    """ View da tabelas contendo os Alunos Cadastrados.
    """
    return render(request, 'alunos_cadastrados.html')


def cadastro_aluno(request):
    """ View do formulario de cadastro de aluno.
    """
    return render(request, 'cadastro_aluno.html')
