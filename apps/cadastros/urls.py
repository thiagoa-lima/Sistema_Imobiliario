from django.urls import path
from .views import IndexView, SobreView, BootView

from .views import ClientesCreate, ImoveisCreate
from .views import ClientesUpdate, ImoveisUpdate
from .views import ClientesDelete, ImoveisDelete
from .views import ClientesList, ImoveisList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('bootstrap/', BootView.as_view(), name='boot'),
    
    # ==================================================================================
    # ------ CLIENTES ------------------------------------------------------------------
    # ==================================================================================

    path('clientes/listar/', ClientesList.as_view(), name='listar-clientes'),
    path('clientes/cadastrar/', ClientesCreate.as_view(), name='cadastrar-clientes'),
    path('clientes/editar/<int:pk>', ClientesUpdate.as_view(), name='editar-clientes'),
    path('clientes/excluir/<int:pk>', ClientesDelete.as_view(), name='excluir-clientes'),
    
    # ==================================================================================
    # ------ IMÓVEIS -------------------------------------------------------------------
    # ==================================================================================

    path('imoveis/listar/', ImoveisList.as_view(), name='listar-imoveis'),
    path('imoveis/cadastrar/', ImoveisCreate.as_view(), name='cadastrar-imoveis'),
    path('imoveis/editar/<int:pk>', ImoveisUpdate.as_view(), name='editar-imoveis'),
    path('imoveis/excluir/<int:pk>', ImoveisDelete.as_view(), name='excluir-imoveis'),
    
    # ==================================================================================
    # DELETE ('D' - CRUD)
    # ==================================================================================




  

]