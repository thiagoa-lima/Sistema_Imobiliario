from django.contrib import admin
from apps.cadastros.models import Clientes, Imoveis
from apps.cadastros.forms import ClientesFormAdmin, ImoveisFormAdmin

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):

    # -------------------------------------------------------------------------------------------------------------------------
    # Busca informação do forms.py para usar a mascara de entradas cadastradas no formulário em vez de usar as opções do django
    # -------------------------------------------------------------------------------------------------------------------------
    
    form = ClientesFormAdmin

    class Media:
        js = ('jquery.mask.min.js', "custom.js")

    # ----------------------------------------------------------------
    # Edita informaçõe da tela inicial do cadastro de clientes (ADMIN)
    # ----------------------------------------------------------------
    
    list_display = ('nome', 'tipo_cliente', 'qualificacao', 'telefone',  'celular', 'email',)

    search_fields = ('nome', 'email')
    # list_filter = ('qualificacao', )
    list_per_page = 20

    # --------------------------------------------------
    # Informaçõe usadas pelo JAZZMIN (DIVISÃO DE CAMPOS)
    # --------------------------------------------------

    fieldsets = (
        ("Informações Iniciais", {'fields': ('tipo_cliente', 'cpf', 'nome', 'qualificacao', )}),
        ('Dados de Contato', {'fields': ('telefone', 'celular', 'email')}),
        ('Filiação', {'fields': ('pai', 'mae', )}),
        ('Outras Informações', {'fields': ('rg', 'orgao_expedidor', 'data_expedicao', 'sexo', 'nascimento', 'estado_civil', 'nacionalidade', 'naturalidade',)}),
        ("Dados do Cônjuge", {'fields': ('nome_conjunge', 'cpf_conjuge', 'rg_conjuge', 'orgao_expedidor_conjuge', 'data_expedicao_conjuge', 'sexo_conjuge', 'profissao_conjuge', 'telefone_conjuge', 'celular_conjuge', 'email_conjuge', )}),
        ("Endereço Residencial", {'fields': ('cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf', )}),
    )
    # Order the sections within the change form
    # jazzmin_section_order = ("book loans", "general", "other")


@admin.register(Imoveis)
class ImoveisAdmin(admin.ModelAdmin):

    # -------------------------------------------------------------------------------------------------------------------------
    # Busca informação do forms.py para usar a mascara de entradas cadastradas no formulário em vez de usar as opções do django
    # -------------------------------------------------------------------------------------------------------------------------
    
    form = ImoveisFormAdmin

    class Media:
        js = ('jquery.mask.min.js', "custom.js")

    # ----------------------------------------------------------------
    # Edita informaçõe da tela inicial do cadastro de clientes (ADMIN)
    # ----------------------------------------------------------------

    list_display = ('proprietario', 'endereco', 'numero', 'complemento', 'cidade', 'uf', 'tipo', )
    # search_fields = ('tipo',)
    # list_filter = ('tipo', )
    list_per_page = 20

    # --------------------------------------------------
    # Informaçõe usadas pelo JAZZMIN (DIVISÃO DE CAMPOS)
    # --------------------------------------------------

    fieldsets = (
        ("Informações Iniciais", {'fields': ('proprietario', 'tipo', )}),
        ('Dados do Imóvel', {'fields': ('cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf', )}),
    )
    # Order the sections within the change form
    # jazzmin_section_order = ("book loans", "general", "other")
