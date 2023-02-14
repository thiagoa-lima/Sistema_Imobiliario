from django.contrib import admin
from apps.contratos.models import Administracao, Financeiro_do_Contrato
# Register your models here.

@admin.register(Administracao)
class AdministracaoAdmin(admin.ModelAdmin):
    list_display = ('proprietario', 'imovel', 'data_inicial', 'repasse_garantido')
    # search_fields = ('proprietario',)
    list_filter = ('proprietario', )
    list_per_page = 20

@admin.register(Financeiro_do_Contrato)
class Financeiro_do_Aluguel(admin.ModelAdmin):
    list_display = ('contrato', 'parcela')
    # search_fields = ('proprietario',)
    list_filter = ('contrato', )
    list_per_page = 20