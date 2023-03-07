from django.urls import path

from apps.contratos.views import *
from apps.contratos import views

# app_name = 'contratos'

urlpatterns = [
    
    # CONTRATO DE ADMINITRAÇÃO (CRUD) 
    path('contratos/administracao/', Administracao_List.as_view(), name='contrato-administracao-listar'),
    path('contratos/administracao/cadastrar', Administracao_Create.as_view(), name='contrato-administracao-cadastrar'),
    path('contratos/administracao/editar/<int:pk>', Administracao_Update.as_view(), name='contrato-administracao-editar'),
    path('contratos/administracao/excluir/<int:pk>', Administracao_Delete.as_view(), name='contrato-administracao-excluir'),

    # CONTRATO DE ALUGUEL (CRUD)
    path('contratos/aluguel/', Contrato_Aluguel_List.as_view(), name='contrato-aluguel-listar'),
    path('contratos/aluguel/cadastrar', Contrato_Aluguel_Create.as_view(), name='contrato-aluguel-cadastrar'),
    path('contratos/aluguel/editar/<int:pk>', Contrato_Aluguel_Update.as_view(), name='contrato-aluguel-editar'),
    path('contratos/aluguel/excluir/<int:pk>', Contrato_Aluguel_Delete.as_view(), name='contrato-aluguel-excluir'),

    # CONTRATO DE ALUGUEL (DETALHES)
    path('contratos/aluguel/detalhes/teste/<int:pk>', Detalhes_Contrato_Aluguel_List.as_view(), name='detalhes-teste' ),

    path('contratos/aluguel/detalhes/<int:pk>', views.detalhar_e_gerar_parcelas, name='financeiro-do-contrato-listar' ),
    path('contratos/aluguel/detalhes/parcela/editar/<int:pk>', Financeiro_do_Contrato_Aluguel_Update.as_view(), name='financeiro-do-contrato-aluguel-editar'),
    path('contratos/aluguel/detalhes/parcela/excluir/<int:pk>', Financeiro_do_Contrato_Aluguel_Delete.as_view(), name='financeiro-do-contrato-aluguel-excluir'),
    path('contratos/aluguel/detalhes/repasse/editar/<int:pk>', Financeiro_do_Contrato_Repasse_Update.as_view(), name='financeiro-do-contrato-editar'),

    # RECEITAS - A RECEBER
    path('receitas/a-receber/', Receitas_a_Receber_List.as_view(), name='receitas-a-receber-listar'),
    path('receitas/a-receber/editar<int:pk>', Receitas_a_Receber_Update.as_view(), name='receitas-a-receber-editar'),

    # RECEITAS - RECEBIDAS
    path('receitas/recebidas/', Receitas_Recebidas_List.as_view(), name='receitas-recebidas-listar' ),
    path('receitas/recebidas/editar<int:pk>', Receitas_Recebidas_Update.as_view(), name='receitas-recebidas-editar'),

    # DESPESAS - A REPASSAR
    path('despesas/alugueis/repasses/', Despesas_a_Repassar_List.as_view(), name='despesas-a-repassar-listar'),
    path('despesas/alugueis/repasses/baixar/<int:pk>', Despesas_a_Repassar_Update.as_view(), name='despesas-a-repassar-editar'),

    path('teste_index', views.index_teste, name='teste_index'),
]