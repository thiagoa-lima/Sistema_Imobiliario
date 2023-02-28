from django.urls import path
from .views import AdministracaoList, AluguelList, Receita_Alugueis_a_Receber_List, Receita_Alugueis_Recebidos_List, Lista_parcela_aluguel
from .views import AdministracaoCreate, AluguelCreate, Despesa_Alugueis_a_Repassar_List, Baixa_de_Repasse_Aluguel
from .views import AdministracaoUpdate, AluguelUpdate, Baixa_de_Parcela_Aluguel
from .views import AdministracaoDelete, AluguelDelete
from apps.contratos import views

# app_name = 'contratos'

urlpatterns = [
    path('contratos-administracao/listar', AdministracaoList.as_view(), name='contrato-administracao-listar'),
    path('contratos-administracao/cadastrar', AdministracaoCreate.as_view(), name='contrato-administracao-cadastrar'),
    path('contratos-administracao/editar/<int:pk>', AdministracaoUpdate.as_view(), name='contrato-administracao-editar'),
    path('contratos-administracao/excluir/<int:pk>', AdministracaoDelete.as_view(), name='contrato-administracao-excluir'),

    path('contratos-aluguel/cadastrar', AluguelCreate.as_view(), name='contrato-aluguel-cadastrar'),
    path('contratos-aluguel/listar', AluguelList.as_view(), name='contrato-aluguel-listar'),
    path('contratos-aluguel/excluir/<int:pk>', AluguelDelete.as_view(), name='contrato-aluguel-excluir'),
    path('contratos-aluguel/editar/<int:pk>', AluguelUpdate.as_view(), name='contrato-aluguel-editar'),

    path('contratos-aluguel/financeiro/editar/<int:pk>', Baixa_de_Parcela_Aluguel.as_view(), name='financeiro-do-contrato-editar'),
    path('contratos-aluguel/financeiro/listar/<int:pk>', views.Lista_parcela_aluguel, name='financeiro-do-contrato-listar' ),

    path('receitas/alugueis/a-receber/', Receita_Alugueis_a_Receber_List.as_view(), name='receitas-alugueis-listar' ),
    path('receitas/alugueis/recebidos/', Receita_Alugueis_Recebidos_List.as_view(), name='receitas-alugueis-recebidos-listar' ),

    path('despesas/alugueis/repasses/', views.Despesa_Alugueis_a_Repassar_List, name='despesas-alugueis-repassar-listar'),
    path('despesas/alugueis/repasses/baixar/<int:pk>', Baixa_de_Repasse_Aluguel.as_view(), name='despesas-alugueis-repassar-baixar'),

]