from django.contrib import admin
from apps.contratos.models import Administracao
# Register your models here.

@admin.register(Administracao)
class AdministracaoAdmin(admin.ModelAdmin):
    list_display = ('proprietario', 'imovel', 'data_inicial', 'repasse_garantido')
    # search_fields = ('proprietario',)
    list_filter = ('proprietario', )
    list_per_page = 20