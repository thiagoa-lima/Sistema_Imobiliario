from django.urls import path

# from .views import ClientesCreate, ImoveisCreate
# from .views import ClientesUpdate, ImoveisUpdate
# from .views import ClientesDelete, ImoveisDelete
from .views import Fin_Aluguel_List

urlpatterns = [
   
    # ==================================================================================
    # ------ FINANCEIRO ALUGUEL --------------------------------------------------------
    # ==================================================================================

    path('financeiro_aluguel/listar/<int:pk>', Fin_Aluguel_List.as_view(), name='listar-financeiro_aluguel'),
    # path('clientes/cadastrar/', ClientesCreate.as_view(), name='cadastrar-clientes'),
    # path('clientes/editar/<int:pk>', ClientesUpdate.as_view(), name='editar-clientes'),
    # path('clientes/excluir/<int:pk>', ClientesDelete.as_view(), name='excluir-clientes'),
    
    
]