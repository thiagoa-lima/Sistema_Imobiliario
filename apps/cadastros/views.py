from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # usada para cadastros
from django.views.generic.list import ListView # usada para fazer listas
from .models import Imoveis, Clientes, ClientePF, Clientesssss_PJ
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
# ------ CLIENTES LISTA -------------------------------------------------------------
# ===================================================================================

class Clientes_List(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Clientes
    template_name = 'cadastros/clientes/lista.html'

# ===================================================================================
# ------ CLIENTES PAGAR -------------------------------------------------------------
# ===================================================================================

class Clientes_Delete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Clientes
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('listar-clientes')

# ===================================================================================
# ------ CLIENTES PF ----------------------------------------------------------------
# ===================================================================================

class Clientes_PF_Create(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = ClientePF
   
    fields = '__all__'
    template_name = 'cadastros/clientes/form_PF.html'
    success_url = reverse_lazy('listar-clientes')

    # ALTERA OS CAMPOS NO FORMULÁRIO
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Clientes - Pessoa Física"
        context['botao'] = "Cadastrar"
        
        return context  

class Clientes_PF_Update(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = ClientePF
    fields = '__all__'
    template_name = 'cadastros/clientes/form_PF.html'
    success_url = reverse_lazy('listar-clientes')

    # ALTERA OS CAMPOS NO FORMULÁRIO
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cliente - Pessoa Física"
        context['botao'] = "Salvar"

        return context 

# ===================================================================================
# ------ CLIENTES PJ ----------------------------------------------------------------
# ===================================================================================

class Clientes_PJ_Create(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Clientesssss_PJ
    form_class = forms.Clientes_PJ_Form
    template_name = 'cadastros/clientes/form_PJ.html'
    success_url = reverse_lazy('listar-clientes')

    # O método abaixo serve para alterar os campos dentro dos formulários.
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Clientes - Pessoa Jurídica"
        context['botao'] = "Cadastrar"
        
        return context  

class Clientes_PJ_Update(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Clientesssss_PJ
    form_class = forms.Clientes_PJ_Form
    template_name = 'cadastros/clientes/form_PJ.html'
    success_url = reverse_lazy('listar-clientes')

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Clientes - Pessoa Jurídica"
        context['botao'] = "Cadastrar"
        
        return context  

class Clientes_PJ_Delete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Clientes
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('listar-clientes')

# ===================================================================================
# ------ IMÓVEIS --------------------------------------------------------------------
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
