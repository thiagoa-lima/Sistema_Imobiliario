from django.contrib import admin
from apps.cadastros.models import Clientes, ClientePF, Imoveis, Clientesssss_PJ
from apps.cadastros.forms import ClientesFormAdmin, ImoveisFormAdmin

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Clientesssss_PJ)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'nome',)

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

@admin.register(ClientePF)
class ClientesAdmin(admin.ModelAdmin):

    form = ClientesFormAdmin

    class Media:
        js = ('jquery.mask.min.js', "mask.js")

    list_display = ('cpf', 'nome',)
    search_fields = ('cpf', 'nome',)
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
