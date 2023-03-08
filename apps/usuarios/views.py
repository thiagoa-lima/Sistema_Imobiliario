from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from django.views.generic.list import ListView # usada para fazer listas
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UsuariosForm, Usuarios_Update_Form

# importa o reverse_lazy para direcionar qual url quer ir
from django.urls import reverse_lazy

# CONTROLE DE LOGIN e USUÁRIOS
from django.contrib.auth.mixins import LoginRequiredMixin

# importa o grupo
from django.shortcuts import get_object_or_404

# ===================================================================================
# CREATE ('C' CRUD)
# ===================================================================================

class Usuarios_Create(LoginRequiredMixin, CreateView):
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

class Usuarios_Update(LoginRequiredMixin, UpdateView):
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

class Usuarios_Delete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'usuarios/form-excluir.html'
    success_url = reverse_lazy('usuarios-listar')

# ===================================================================================
# LIST
# ===================================================================================

class Usuarios_List(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'usuarios/lista.html'

def user_login(request):
    template_name = 'usuarios/login.html'
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('deu caca')

    return render(request, template_name, {})
