from django.contrib import admin
from apps.cadastros.models import Clientes, Imoveis

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_cliente', 'qualificacao', 'telefone',  'celular', 'email',)
    search_fields = ('nome', 'email')
    # list_filter = ('qualificacao', )
    list_per_page = 20

@admin.register(Imoveis)
class ImoveisAdmin(admin.ModelAdmin):
    list_display = ('proprietario', 'endereco', 'numero', 'complemento', 'cidade', 'uf', 'tipo', )
    # search_fields = ('tipo',)
    # list_filter = ('tipo', )
    list_per_page = 20
