from django.urls import path
from .views import AdministracaoCreate
from .views import AdministracaoList


urlpatterns = [
    path('contratos-administracao/listar', AdministracaoList.as_view(), name='contrato-administracao-listar'),
    path('contratos-administracao/cadastrar', AdministracaoCreate.as_view(), name='contrato-administracao-cadastrar')
]