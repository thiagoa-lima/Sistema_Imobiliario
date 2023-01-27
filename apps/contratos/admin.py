from django.contrib import admin
from apps.contratos.models import Administracao
# Register your models here.

@admin.register(Administracao)
class Contrato_AdministracaoAdmin(admin.ModelAdmin):
    list_display = ('proprietario', )
    search_fields = ('proprietario',)
    list_filter = ('proprietario', )
    list_per_page = 20