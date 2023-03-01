from django.urls import path
from .views import AdministracaoList, AluguelList, Receita_Alugueis_a_Receber_List, Receita_Alugueis_Recebidos_List, Lista_parcela_aluguel
from .views import AdministracaoCreate, AluguelCreate, Despesa_Alugueis_a_Repassar_List
from .views import AdministracaoUpdate, AluguelUpdate
from .views import AdministracaoDelete, AluguelDelete

from .views import Financeiro_do_Contrato_Aluguel_DELETE, Financeiro_do_Contrato_Aluguel_UPDATE
from .views import Financeiro_do_Contrato_Repasse_UPDATE
from apps.contratos import views

# app_name = 'contratos'

urlpatterns = [
    path('contratos/administracao/', AdministracaoList.as_view(), name='contrato-administracao-listar'),
    path('contratos/administracao/cadastrar', AdministracaoCreate.as_view(), name='contrato-administracao-cadastrar'),
    path('contratos/administracao/editar/<int:pk>', AdministracaoUpdate.as_view(), name='contrato-administracao-editar'),
    path('contratos/administracao/excluir/<int:pk>', AdministracaoDelete.as_view(), name='contrato-administracao-excluir'),

    path('contratos/aluguel/', AluguelList.as_view(), name='contrato-aluguel-listar'),
    path('contratos/aluguel/cadastrar', AluguelCreate.as_view(), name='contrato-aluguel-cadastrar'),
    path('contratos/aluguel/editar/<int:pk>', AluguelUpdate.as_view(), name='contrato-aluguel-editar'),
    path('contratos/aluguel/excluir/<int:pk>', AluguelDelete.as_view(), name='contrato-aluguel-excluir'),

    path('contratos/aluguel/detalhes/<int:pk>', views.Lista_parcela_aluguel, name='financeiro-do-contrato-listar' ),
    path('contratos/aluguel/detalhes/parcela/editar/<int:pk>', Financeiro_do_Contrato_Aluguel_UPDATE.as_view(), name='financeiro-do-contrato-aluguel-editar'),
    path('contratos/aluguel/detalhes/parcela/excluir/<int:pk>', Financeiro_do_Contrato_Aluguel_DELETE.as_view(), name='financeiro-do-contrato-aluguel-excluir'),
    path('contratos/aluguel/detalhes/repasse/editar/<int:pk>', Financeiro_do_Contrato_Repasse_UPDATE.as_view(), name='financeiro-do-contrato-editar'),
    # path('contratos/aluguel/detalhes/repasse/excluir/<int:pk>', .as_view(), name='financeiro-do-contrato-aluguel-excluir'),

    path('receitas/alugueis/a-receber/', Receita_Alugueis_a_Receber_List.as_view(), name='receitas-alugueis-listar' ),
    path('receitas/alugueis/recebidos/', Receita_Alugueis_Recebidos_List.as_view(), name='receitas-alugueis-recebidos-listar' ),

    path('despesas/alugueis/repasses/', views.Despesa_Alugueis_a_Repassar_List, name='despesas-alugueis-repassar-listar'),
    path('despesas/alugueis/repasses/baixar/<int:pk>', Financeiro_do_Contrato_Repasse_UPDATE.as_view(), name='despesas-alugueis-repassar-baixar'),

]