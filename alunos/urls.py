from django.urls import path
from . import views


urlpatterns = [
    path('', views.alunos_cadastrados, name='index'),
    path('alunos_cadastrados/', views.alunos_cadastrados, name='alunos_cadastrados'),
    path('cadastro_aluno/', views.cadastro_aluno, name='cadastro_aluno'),
]
