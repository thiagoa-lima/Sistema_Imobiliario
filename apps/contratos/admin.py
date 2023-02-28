from django.contrib import admin
from apps.contratos.models import Administracao, Financeiro_do_Contrato, Aluguel
# Register your models here.

@admin.register(Administracao)
class AdministracaoAdmin(admin.ModelAdmin):
    list_display = ('proprietario', 'imovel', 'data_inicial')
    # search_fields = ('proprietario',)
    list_filter = ('proprietario', )
    list_per_page = 20

@admin.register(Financeiro_do_Contrato)
class Financeiro_do_Aluguel(admin.ModelAdmin):
    list_display = ('id', 'contrato', 'parcela',)
    # search_fields = ('proprietario',)
    list_filter = ('contrato', )
    list_per_page = 20

@admin.register(Aluguel)
class Aluguel_Admin(admin.ModelAdmin):
    list_display = ('id', 'proprietario', 'imovel', 'locatario')
    # search_fields = ('proprietario',)
