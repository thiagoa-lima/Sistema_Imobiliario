from django.contrib import admin
from apps.administrativo.models import Painel
# Register your models here.


@admin.register(Painel)
class Painel_Admin(admin.ModelAdmin):
    list_display = ('cpf_cnpj', 'nome_empresa', 'nome_fantasia')