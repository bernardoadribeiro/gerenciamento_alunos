from django.urls import path
from . import views


urlpatterns = [
    path('', views.alunos, name='index'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
]
