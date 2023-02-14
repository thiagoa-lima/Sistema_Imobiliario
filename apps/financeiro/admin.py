from django.contrib import admin
from apps.financeiro.models import Fin_Aluguel
# Register your models here.

@admin.register(Fin_Aluguel)
class Fin_Aluguel_Admin(admin.ModelAdmin):
    list_display = ('contrato', 'vencimento', 'parcela', 'multa')
    # search_fields = ('proprietario',)
    list_filter = ('contrato', )
    list_per_page = 20