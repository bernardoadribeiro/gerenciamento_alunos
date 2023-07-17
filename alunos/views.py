from datetime import date
import os

from django.shortcuts import redirect, render
from django.contrib import messages

from config.settings import BASE_DIR

from .models import Aluno
from .forms import AlunoModelForm

from markdown import markdown


# Create your views here.

def index(request):
    """ View Index.
        Exibe o arquivo localizado em `/config/templates/index.html`
    """
    # abre o arquivo `README.md` e le o conteudo do readme
    with open(os.path.join(BASE_DIR, 'README.md'), 'r', encoding='UTF-8') as readme_file:
        readme_content = readme_file.read()

    # converte o conteudo em markdown para html
    index_content = markdown(readme_content)

    context = {
        'index_content': index_content,
    }

    return render(request, 'index.html', context)


def unauthorized(request):
    return render(request, 'unauthorized.html')


def alunos(request):
    """ View da tabelas contendo os Alunos Cadastrados.
    """
    if str(request.user) == 'AnonymousUser':
        # retorna erro 401 (Unauthorized) quando o usuario acessar a rota que nao possui permissao.
        return redirect('/unauthorized')
    else:
        alunos = Aluno.objects.all()

        for aluno in alunos:
            idade = (date.today() - aluno.data_nascimento).days // 365
            aluno.idade = idade

        form = AlunoModelForm()

        context = {
            'alunos': alunos,
            'form': form,
            'form_url': 'cadastrar_aluno/'
        }

    return render(request, 'alunos_cadastrados.html', context)


def cadastrar_aluno(request):
    """ View do formulario de cadastro de aluno.
    """

    form = AlunoModelForm(request.POST, request.FILES)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'Aluno cadastrado.')
        else:
            messages.error(request, 'Erro ao cadastrar o aluno. Tente novamente.')

    return redirect('/alunos')
