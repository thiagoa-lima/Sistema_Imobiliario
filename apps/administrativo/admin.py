from django.contrib import admin
from apps.administrativo.models import Painel_administrativo
# Register your models here.

@admin.register(Painel_administrativo)
class Painel_Admin(admin.ModelAdmin):
    list_display = ('cpf_cnpj', 'nome_empresa', 'nome_fantasia')