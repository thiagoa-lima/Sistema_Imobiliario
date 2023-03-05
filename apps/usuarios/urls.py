from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
    path('usuarios/', Usuarios_List.as_view(), name='usuarios-listar'),
    path('usuarios/cadastrar/', Usuarios_Create.as_view(), name='usuarios-cadastrar'),
    path('usuarios/editar/<int:pk>', Usuarios_Update.as_view(), name='usuarios-editar'),
    path('excluir/usuarios/<int:pk>', Usuarios_Delete.as_view(), name='usuarios-excluir'),

]