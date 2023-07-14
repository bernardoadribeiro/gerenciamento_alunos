from django.contrib import admin

from alunos.models import Aluno


# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'data_nascimento', 'data_ingresso',)
    # list_filter = ('nome', 'curso',)
    search_fields = ('nome', 'curso',)
