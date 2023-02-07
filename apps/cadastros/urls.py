from django.urls import path
from .views import IndexView, SobreView, BootView

from .views import ClientesCreate, ImoveisCreate
from .views import ClientesUpdate
from .views import ClientesDelete
from .views import ClientesList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('bootstrap/', BootView.as_view(), name='boot'),
    
    # ==================================================================================
    # CREATE ('C' - CRUD)
    # ==================================================================================

    path('cadastrar/cliente/', ClientesCreate.as_view(), name='cadastrar-cliente'),
    path('cadastrar/imovel/', ImoveisCreate.as_view(), name='cadastrar-imovel'),

    # ==================================================================================
    # UPDATE ('U' - CRUD)
    # ==================================================================================

    path('editar/cliente/<int:pk>', ClientesUpdate.as_view(), name='editar-cliente'),


    # ==================================================================================
    # DELETE ('D' - CRUD)
    # ==================================================================================

    path('excluir/cliente/<int:pk>', ClientesDelete.as_view(), name='excluir-cliente'),

    # ==================================================================================
    # LIST
    # ==================================================================================

    path('listar/clientes/', ClientesList.as_view(), name='listar-clientes'),

]