from django.contrib import admin
from .models import Sorteio, Pessoa
# Register your models here.

@admin.register(Sorteio)
class SorteioAdmin(admin.ModelAdmin):
    list_display = ['premio', 'post_instagram', 'perfil_instagram']

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone']