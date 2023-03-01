from django.urls import path
from .views import AdministracaoList, AdministracaoCreate, AdministracaoUpdate, AdministracaoDelete
from .views import Financeiro_do_Contrato_Aluguel_DELETE, Financeiro_do_Contrato_Aluguel_UPDATE, Financeiro_do_Contrato_Repasse_UPDATE
from .views import Contrato_Aluguel_CREATE, Contrato_Aluguel_UPDATE, Contrato_Aluguel_DELETE, Contrato_Aluguel_LIST, Contrato_Aluguel_DETALHES
from .views import Receitas_a_Receber_LIST, Receitas_a_Receber_UPDATE, Receitas_Recebidas_LIST, Receitas_Recebidas_UPDATE
from .views import Despesas_a_Repassar_LIST

from apps.contratos import views

# app_name = 'contratos'

urlpatterns = [
    path('contratos/administracao/', AdministracaoList.as_view(), name='contrato-administracao-listar'),
    path('contratos/administracao/cadastrar', AdministracaoCreate.as_view(), name='contrato-administracao-cadastrar'),
    path('contratos/administracao/editar/<int:pk>', AdministracaoUpdate.as_view(), name='contrato-administracao-editar'),
    path('contratos/administracao/excluir/<int:pk>', AdministracaoDelete.as_view(), name='contrato-administracao-excluir'),

    # CONTRATO DE ALUGUEL (CRUD)
    path('contratos/aluguel/', Contrato_Aluguel_LIST.as_view(), name='contrato-aluguel-listar'),
    path('contratos/aluguel/cadastrar', Contrato_Aluguel_CREATE.as_view(), name='contrato-aluguel-cadastrar'),
    path('contratos/aluguel/editar/<int:pk>', Contrato_Aluguel_UPDATE.as_view(), name='contrato-aluguel-editar'),
    path('contratos/aluguel/excluir/<int:pk>', Contrato_Aluguel_DELETE.as_view(), name='contrato-aluguel-excluir'),

    # CONTRATO DE ALUGUEL (DETALHES)
    path('contratos/aluguel/detalhes/<int:pk>', views.Contrato_Aluguel_DETALHES, name='financeiro-do-contrato-listar' ),
    path('contratos/aluguel/detalhes/parcela/editar/<int:pk>', Financeiro_do_Contrato_Aluguel_UPDATE.as_view(), name='financeiro-do-contrato-aluguel-editar'),
    path('contratos/aluguel/detalhes/parcela/excluir/<int:pk>', Financeiro_do_Contrato_Aluguel_DELETE.as_view(), name='financeiro-do-contrato-aluguel-excluir'),
    path('contratos/aluguel/detalhes/repasse/editar/<int:pk>', Financeiro_do_Contrato_Repasse_UPDATE.as_view(), name='financeiro-do-contrato-editar'),

    # RECEITAS - A RECEBER
    path('receitas/a-receber/', Receitas_a_Receber_LIST.as_view(), name='receitas-a-receber-listar'),
    path('receitas/a-receber/editar<int:pk>', Receitas_a_Receber_UPDATE.as_view(), name='receitas-a-receber-editar'),

    # RECEITAS - RECEBIDAS
    path('receitas/recebidas/', Receitas_Recebidas_LIST.as_view(), name='receitas-recebidas-listar' ),
    path('receitas/recebidas/editar<int:pk>', Receitas_Recebidas_UPDATE.as_view(), name='receitas-recebidas-editar'),

    # DESPESAS - A REPASSAR
    path('despesas/alugueis/repasses/', Despesas_a_Repassar_LIST.as_view(), name='despesas-a-repassar-listar'),
    path('despesas/alugueis/repasses/baixar/<int:pk>', Financeiro_do_Contrato_Repasse_UPDATE.as_view(), name='despesas-alugueis-repassar-baixar'),

]