from django.contrib import admin
from apps.cadastros.models import Clientes, Clientes_PF, Imoveis, Clientesssss_PF
from apps.cadastros.forms import ClientesFormAdmin, ImoveisFormAdmin

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Clientesssss_PF)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome',)

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

@admin.register(Clientes_PF)
class ClientesAdmin(admin.ModelAdmin):

    # -------------------------------------------------------------------------------------------------------------------------
    # Busca informação do forms.py para usar a mascara de entradas cadastradas no formulário em vez de usar as opções do django
    # -------------------------------------------------------------------------------------------------------------------------
    
    form = ClientesFormAdmin

    class Media:
        js = ('jquery.mask.min.js', "mask.js")

    # ----------------------------------------------------------------
    # Edita informaçõe da tela inicial do cadastro de clientes (ADMIN)
    # ----------------------------------------------------------------
    
    list_display = ('nome', 'tipo_cliente', 'qualificacao', 'telefone',  'celular', 'email',)

    search_fields = ('nome', 'email')
    # list_filter = ('qualificacao', )
    list_per_page = 20


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

