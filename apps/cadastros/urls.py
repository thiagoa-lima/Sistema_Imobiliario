from django.urls import path
from .views import IndexView, SobreView, BootView

from .views import Clientes_PF_Create, ImoveisCreate
from .views import Clientes_PF_Update, ImoveisUpdate
from .views import Clientes_PF_Delete, ImoveisDelete
from .views import Clientes_PF_List, ImoveisList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('bootstrap/', BootView.as_view(), name='boot'),
    
    # ==================================================================================
    # ------ Clientes_PF ---------------------------------------------------------------
    # ==================================================================================

    path('clientes/pf/listar/', Clientes_PF_List.as_view(), name='listar-clientes'),
    path('clientes/pf/cadastrar/', Clientes_PF_Create.as_view(), name='cadastrar-clientes'),
    path('clientes/pf/editar/<int:pk>', Clientes_PF_Update.as_view(), name='editar-clientes'),
    path('clientes/pf/excluir/<int:pk>', Clientes_PF_Delete.as_view(), name='excluir-clientes'),
    
    # ==================================================================================
    # ------ IMÓVEIS -------------------------------------------------------------------
    # ==================================================================================

    path('imoveis/listar/', ImoveisList.as_view(), name='listar-imoveis'),
    path('imoveis/cadastrar/', ImoveisCreate.as_view(), name='cadastrar-imoveis'),
    path('imoveis/editar/<int:pk>', ImoveisUpdate.as_view(), name='editar-imoveis'),
    path('imoveis/excluir/<int:pk>', ImoveisDelete.as_view(), name='excluir-imoveis'),
    
]