from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuariosCreate, UsuariosList, UsuariosUpdate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('excluir/usuarios/<int:pk>', UsuariosUpdate.as_view(), name='excluir-usuario'),

    path('usuarios/editar/<int:pk>', UsuariosUpdate.as_view(), name='usuarios-editar'),
    path('usuarios/', UsuariosList.as_view(), name='usuarios-listar'),
    path('usuarios/cadastrar/', UsuariosCreate.as_view(), name='usuarios-cadastrar'),
]