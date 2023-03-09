from django.urls import path
from .views import Painel_Administrativo_View

# app_name = 'contratos'

urlpatterns = [
    path('painel-administrativo/<int:pk>', Painel_Administrativo_View.as_view(), name='painel-administrativo'),
]