from django import forms


class AlunoForm(forms.Form):
    """ Formulario para inserir novo aluno """

    nome = forms.CharField(label="Nome do aluno", max_length=100),
    foto_perfil = forms.CharField(label="Foto de perfil", max_length=256)
    cpf = forms.CharField(label="CPF", max_length=11)  # Desconsidera pontuacao
    rg = forms.CharField(label="RG", max_length=10)   # Desconsidera pontuacao
    curso = forms.CharField(label="Curso", max_length=100)
    data_nascimento = forms.DateField(label="Data de Nascimento",)
    data_ingresso = forms.DateField(label="Data de ingresso",)
