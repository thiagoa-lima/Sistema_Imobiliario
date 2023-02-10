from django.urls import path
from .views import AdministracaoCreate, AluguelCreate
from .views import AdministracaoList, AluguelList
from .views import AluguelDelete
from .views import AluguelUpdate

# app_name = 'contratos'

urlpatterns = [
    path('contratos-administracao/listar', AdministracaoList.as_view(), name='contrato-administracao-listar'),
    path('contratos-administracao/cadastrar', AdministracaoCreate.as_view(), name='contrato-administracao-cadastrar'),

    path('contratos-aluguel/cadastrar', AluguelCreate.as_view(), name='contrato-aluguel-cadastrar'),
    path('contratos-aluguel/listar', AluguelList.as_view(), name='contrato-aluguel-listar'),
    path('contratos-aluguel/excluir/<int:pk>', AluguelDelete.as_view(), name='contrato-aluguel-excluir'),
    path('contratos-aluguel/editar/<int:pk>', AluguelUpdate.as_view(), name='contrato-aluguel-editar'),
]