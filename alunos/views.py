from datetime import date
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Aluno
from .forms import AlunoForm


# Create your views here.

def index(request):
    """ View Index.
        Exibe o arquivo localizado em `/config/templates/index.html`
    """
    return render(request, 'index.html')


def alunos(request):
    """ View da tabelas contendo os Alunos Cadastrados.
    """
    alunos = Aluno.objects.all()

    for aluno in alunos:
        idade = (date.today() - aluno.data_nascimento).days // 365
        aluno.idade = idade

    form = AlunoForm(request.POST or None)

    context = {
        'alunos': alunos,
        'form': form,
        'form_url': 'cadastrar_aluno/'
    }

    return render(request, 'alunos_cadastrados.html', context)


def cadastrar_aluno(request):
    """ View do formulario de cadastro de aluno.
    """

    form = AlunoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = request.POST.get('nome')
            foto_perfil = request.POST.get('foto_perfil')
            cpf = request.POST.get('cpf')
            rg = request.POST.get('rg')
            curso = request.POST.get('curso')
            data_nascimento = request.POST.get('data_nascimento')
            data_ingresso = request.POST.get('data_ingresso')

            Aluno.objects.create(nome=nome, foto_perfil=foto_perfil, cpf=cpf, rg=rg, curso=curso,
                                 data_nascimento=data_nascimento, data_ingresso=data_ingresso)

            messages.success(request, 'Aluno cadastrado.')
        else:
            messages.error(request, 'Erro ao cadastrar o aluno. Tente novamente.')

    return redirect('/alunos')
