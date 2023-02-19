from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # usada para cadastros
from django.views.generic.list import ListView # usada para fazer listas
from .models import Clientes_PF, Clientes_PJ, Imoveis, Clientes
from django.urls import reverse_lazy
from . import forms

# CONTROLE DE LOGIN e USÁRIOS
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin 

# ===================================================================================
# CREATE ('C' - CRUD)
# ===================================================================================

  

class ImoveisCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Imoveis
    form_class = forms.ImoveisForm
    template_name = 'cadastros/imoveis/form.html'
    success_url = reverse_lazy('listar-imoveis')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de imóveis"
        context['botao'] = "Cadastrar"
        
        return context 

# ===================================================================================
# ------ Clientes_PF ----------------------------------------------------------------
# ===================================================================================

class Clientes_PF_List(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Clientes
    template_name = 'cadastros/clientes/lista.html'

class Clientes_PF_Create(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Clientes_PF
   
    fields = '__all__'
    template_name = 'cadastros/clientes/pf/form.html'
    success_url = reverse_lazy('listar-clientes')

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Clientes - Pessoa Física"
        context['botao'] = "Cadastrar"
        
        return context  

class Clientes_PF_Update(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Clientes_PF
    fields = '__all__'
    template_name = 'cadastros/clientes/pf/form.html'
    success_url = reverse_lazy('listar-clientes')

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar cadastro de clientes"
        context['botao'] = "Salvar"

        return context 

class Clientes_PF_Delete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Clientes_PF
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('listar-clientes')

# ===================================================================================
# ------ Clientes_PJ ----------------------------------------------------------------
# ===================================================================================

class Clientes_PJ_List(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Clientes_PJ
    template_name = 'cadastros/clientes/pj/lista.html'

class Clientes_PJ_Create(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Clientes_PJ
    fields = '__all__'
    template_name = 'cadastros/clientes/pj/form.html'
    success_url = reverse_lazy('listar-clientes-pj')

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Clientes - Pessoa Jurídica"
        context['botao'] = "Cadastrar"
        
        return context  


# ===================================================================================
# ------ Imóveis --------------------------------------------------------------------
# ===================================================================================

class ImoveisList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Imoveis
    template_name = 'cadastros/imoveis/lista.html'

class ImoveisDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Imoveis
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('listar-imoveis')
  
class ImoveisUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Imoveis
    form_class = forms.ImoveisForm
    template_name = 'cadastros/imoveis/form.html'
    success_url = reverse_lazy('listar-imoveis')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar cadastro de imóveis"
        context['botao'] = "Salvar"
        
        return context 
    




class IndexView(TemplateView):
    template_name = 'base.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'

class BootView(TemplateView):
    template_name = 'boot.html'

class ClientesView(TemplateView):
    template_name = 'padrao/form.html'
