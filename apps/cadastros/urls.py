from django.urls import path
from .views import IndexView, SobreView, BootView

from .views import Clientes_List, ImoveisList
from .views import Clientes_PF_Create, Clientes_PJ_Create, ImoveisCreate
from .views import Clientes_PF_Update, Clientes_PJ_Update, ImoveisUpdate
from .views import Clientes_Delete, ImoveisDelete

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('bootstrap/', BootView.as_view(), name='boot'),
    
    # ==========================================================================================
    # ------ CLIENTES  -------------------------------------------------------------------------
    # ==========================================================================================

    path('clientes/listar/', Clientes_List.as_view(), name='listar-clientes'),
    path('clientes/excluir/<int:pk>', Clientes_Delete.as_view(), name='excluir-clientes'),

    path('clientes/pf/cadastrar/', Clientes_PF_Create.as_view(), name='cadastrar-clientes-pf'),
    path('clientes/pf/editar/<int:pk>', Clientes_PF_Update.as_view(), name='editar-clientes-pf'),

    path('clientes/pj/cadastrar/', Clientes_PJ_Create.as_view(), name='cadastrar-clientes-pj'),
    path('clientes/pj/editar/<int:pk>', Clientes_PJ_Update.as_view(), name='editar-clientes-pj'),

    # ==========================================================================================
    # ------ IMÓVEIS -------------------------------------------------------------------
    # ==========================================================================================

    path('imoveis/listar/', ImoveisList.as_view(), name='listar-imoveis'),
    path('imoveis/cadastrar/', ImoveisCreate.as_view(), name='cadastrar-imoveis'),
    path('imoveis/editar/<int:pk>', ImoveisUpdate.as_view(), name='editar-imoveis'),
    path('imoveis/excluir/<int:pk>', ImoveisDelete.as_view(), name='excluir-imoveis'),
    
]