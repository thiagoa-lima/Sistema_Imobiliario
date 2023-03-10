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

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='usuarios/password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='usuarios/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
  
  
#   path('reset_password/', 
#             auth_views.PasswordResetView.as_view(
#             template_name='usuarios/password_reset_form.html', 
#             html_email_template_name="usuarios/email_reset_template.html",
#             email_template_name='usuarios/password_reset_email.html', 
#             subject_template_name="usuarios/password_reset_subject.txt",
#             ),
#              name="password_reset"),

]