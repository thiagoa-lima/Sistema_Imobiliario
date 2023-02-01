from django.contrib import admin
from apps.cadastros.models import Clientes, Imoveis

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_cliente', 'qualificacao', 'telefone',  'celular', 'email',)
    search_fields = ('nome', 'email')
    # list_filter = ('qualificacao', )
    list_per_page = 20

    fieldsets = (
        ("Informações Iniciais", {'fields': ('tipo_cliente', 'cpf', 'nome', 'qualificacao', )}),
        ('Contatos', {'fields': ('telefone', 'celular', 'email')}),
        ('Filiação', {'fields': ('pai', 'mae', )}),
        ('Outras Informações', {'fields': ('rg', 'orgao_expedidor', 'data_expedicao', 'sexo', 'nascimento', 'estado_civil', 'nacionalidade', 'naturalidade',)}),
        ("Cônjuge", {'fields': ('nome_conjunge', 'cpf_conjuge', 'rg_conjuge', 'orgao_expedidor_conjuge', 'data_expedicao_conjuge', 'sexo_conjuge', 'profissao_conjuge', 'telefone_conjuge', 'celular_conjuge', 'email_conjuge', )}),
        ("Endereço", {'fields': ('cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf', )}),
    )
    # Order the sections within the change form
    # jazzmin_section_order = ("book loans", "general", "other")


@admin.register(Imoveis)
class ImoveisAdmin(admin.ModelAdmin):
    list_display = ('proprietario', 'endereco', 'numero', 'complemento', 'cidade', 'uf', 'tipo', )
    # search_fields = ('tipo',)
    # list_filter = ('tipo', )
    list_per_page = 20
