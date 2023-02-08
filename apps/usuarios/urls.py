from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuariosCreate, UsuariosList, UsuariosUpdate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastrar/usuarios/', UsuariosCreate.as_view(), name='cadastrar-usuarios'),
    path('editar/usuarios/<int:pk>', UsuariosUpdate.as_view(), name='editar-usuario'),
    path('excluir/usuarios/<int:pk>', UsuariosUpdate.as_view(), name='excluir-usuario'),
    path('listar/usuarios/', UsuariosList.as_view(), name='listar-usuarios'),

]