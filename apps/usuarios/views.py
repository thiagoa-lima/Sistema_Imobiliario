from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from django.views.generic.list import ListView # usada para fazer listas

# importa as classes do forms.py
from .forms import UsuariosForm, Usuarios_Update_Form

# importa o reverse_lazy para direcionar qual url quer ir
from django.urls import reverse_lazy

# CONTROLE DE LOGIN e USÁRIOS
from django.contrib.auth.mixins import LoginRequiredMixin

# importa o grupo
from django.shortcuts import get_object_or_404

# ===================================================================================
# CREATE ('C' CRUD)
# ===================================================================================

class UsuariosCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = User
    template_name = "usuarios/form-cadastrar.html"
    form_class = UsuariosForm
    success_url = reverse_lazy('usuarios-listar')

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de novo usuário"
        context['botao'] = "Cadastrar"
        
        return context   

# ===================================================================================
# UPDATE ('U' CRUD)
# ===================================================================================

class UsuariosUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    form_class = Usuarios_Update_Form
    template_name = "usuarios/form-editar.html"
    success_url = reverse_lazy('usuarios-listar')

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar usuário"
        context['botao'] = "Salvar"
        
        return context   

# ===================================================================================
# DELETE ('D' - CRUD)
# ===================================================================================

class UsuariosDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'usuarios/form-excluir.html'
    success_url = reverse_lazy('usuarios-listar')

# ===================================================================================
# LIST
# ===================================================================================

class UsuariosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'usuarios/lista.html'
