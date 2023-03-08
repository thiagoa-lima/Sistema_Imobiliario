from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
    path('usuarios/', Usuarios_List.as_view(), name='usuarios-listar'),
    path('usuarios/cadastrar/', Usuarios_Create.as_view(), name='usuarios-cadastrar'),
    path('usuarios/editar/<int:pk>', Usuarios_Update.as_view(), name='usuarios-editar'),
    path('excluir/usuarios/<int:pk>', Usuarios_Delete.as_view(), name='usuarios-excluir'),

]