from django.urls import path
from .views import IndexView, SobreView, BootView

from .views import Clientes_List, ImoveisList
from .views import Clientes_PF_Create, Clientes_PJ_Create, ImoveisCreate
from .views import Clientes_PF_Update, Clientes_PJ_Update, ImoveisUpdate 
from .views import Clientes_Delete, ImoveisDelete
from .views import Saida_de_Chaves_por_Imovel
from .views import Saida_de_Chaves_LIST, Saida_de_Chaves_CREATE, Saida_de_Chaves_UPDATE, Saida_de_Chaves_DELETE
from apps.cadastros import views


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('bootstrap/', BootView.as_view(), name='boot'),
    
    # CLIENTES
    path('clientes/', Clientes_List.as_view(), name='listar-clientes'),
    path('clientes/excluir/<int:pk>', Clientes_Delete.as_view(), name='excluir-clientes'),

    # CLIENTES PF
    path('clientes/pf/cadastrar/', Clientes_PF_Create.as_view(), name='cadastrar-clientes-pf'),
    path('clientes/pf/editar/<int:pk>', Clientes_PF_Update.as_view(), name='editar-clientes-pf'),

    #CLIENTES PJ
    path('clientes/pj/cadastrar/', Clientes_PJ_Create.as_view(), name='cadastrar-clientes-pj'),
    path('clientes/pj/editar/<int:pk>', Clientes_PJ_Update.as_view(), name='editar-clientes-pj'),

    # IMÓVEIS
    path('imoveis/', ImoveisList.as_view(), name='listar-imoveis'),
    path('imoveis/cadastrar/', ImoveisCreate.as_view(), name='cadastrar-imoveis'),
    path('imoveis/editar/<int:pk>', ImoveisUpdate.as_view(), name='editar-imoveis'),
    path('imoveis/excluir/<int:pk>', ImoveisDelete.as_view(), name='excluir-imoveis'),

    # CHAVES
    path('chaves/', Saida_de_Chaves_LIST.as_view(), name='listar-saida-chaves'),
    path('chaves/cadatrar/', Saida_de_Chaves_CREATE.as_view(), name='cadastrar-saida-chaves'),
    path('chaves/editar/<int:pk>', Saida_de_Chaves_UPDATE.as_view(), name='editar-saida-chaves'),
    path('chaves/excluir/<int:pk>', Saida_de_Chaves_DELETE.as_view(), name='excluir-saida-chaves'),

    # CHAVES POR IMÓVEL
    path('imoveis/chaves/<int:pk>', views.Saida_de_Chaves_por_Imovel, name='listar-controle-chaves'),
]