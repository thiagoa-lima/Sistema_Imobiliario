from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from django.views.generic.list import ListView # usada para fazer listas

# importa as classes do forms.py
from .forms import UsuariosForm

# importa o reverse_lazy para direcionar qual url quer ir
from django.urls import reverse_lazy

# CONTROLE DE LOGIN e USÁRIOS
from django.contrib.auth.mixins import LoginRequiredMixin

# importa o grupo
from django.shortcuts import get_object_or_404

# ===================================================================================
# CREATE ('C' CRUD)
# ===================================================================================

class UsuariosCreate(CreateView):
    template_name = "usuarios/form.html"
    form_class = UsuariosForm
    success_url = reverse_lazy('usuarios-listar')

    # O método abaixo é chamado quando submete um formulário
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='admin')
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de novo usuário"
        context['botao'] = "Cadastrar"
        
        return context   

# ===================================================================================
# UPDATE ('U' CRUD)
# ===================================================================================

class UsuariosUpdate(UpdateView):
    template_name = "usuarios/form.html"
    form_class = UsuariosForm
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

class ClientesDelete(LoginRequiredMixin, DeleteView):
    form_class = UsuariosForm
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('excluir-usuarios')

# ===================================================================================
# LIST
# ===================================================================================

class UsuariosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'usuarios/lista.html'
