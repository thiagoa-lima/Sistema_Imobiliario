from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # usada para cadastros
from django.views.generic.list import ListView # usada para fazer listas

from .models import Clientes, Imoveis

from django.urls import reverse_lazy

# CONTROLE DE LOGIN e USÁRIOS
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin 


# ===================================================================================
# CREATE ('C' - CRUD)
# ===================================================================================

class ClientesCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Clientes
    fields = [
        'cpf', 'nome', 'tipo_cliente', 'qualificacao', 'telefone', 'celular', 'email', 'pai', 'mae',
        'rg', 'orgao_expedidor', 'data_expedicao', 'sexo', 'nascimento', 'estado_civil', 'nacionalidade',
        'naturalidade', 'nome_conjunge', 'cpf_conjuge', 'rg_conjuge', 'orgao_expedidor_conjuge', 
        'data_expedicao_conjuge', 'sexo_conjuge', 'profissao_conjuge', 'telefone_conjuge', 'celular_conjuge',
        'email_conjuge', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf',
    ]
    template_name = 'padrao/form.html'
    success_url = reverse_lazy('listar-clientes')

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de clientes"
        context['botao'] = "Cadastrar"
        
        return context        

class ImoveisCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Imoveis
    fields = ['proprietario', 'tipo', 'cep',]
    template_name = 'padrao/form.html'
    success_url = reverse_lazy('index')

# ===================================================================================
# UPDATE ('U' - CRUD)
# ===================================================================================

class ClientesUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Clientes
    fields = [
        'cpf', 'nome', 'tipo_cliente', 'qualificacao', 'telefone', 'celular', 'email', 'pai', 'mae',
        'rg', 'orgao_expedidor', 'data_expedicao', 'sexo', 'nascimento', 'estado_civil', 'nacionalidade',
        'naturalidade', 'nome_conjunge', 'cpf_conjuge', 'rg_conjuge', 'orgao_expedidor_conjuge', 
        'data_expedicao_conjuge', 'sexo_conjuge', 'profissao_conjuge', 'telefone_conjuge', 'celular_conjuge',
        'email_conjuge', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf',
    ]
    template_name = 'padrao/form.html'
    success_url = reverse_lazy('listar-clientes')

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar cadastro de clientes"
        context['botao'] = "Salvar"

        return context 
    

class ImoveisUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Imoveis
    fields = ['proprietario', 'tipo', 'cep',]
    template_name = 'padrao/form.html'
    success_url = reverse_lazy('index')

# ===================================================================================
# DELETE ('D' - CRUD)
# ===================================================================================

class ClientesDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Clientes
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('listar-clientes')

class ImoveisDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Imoveis
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('index')



# ===================================================================================
# LIST
# ===================================================================================

class ClientesList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Clientes
    template_name = 'cadastros/listas/clientes.html'
    






class IndexView(TemplateView):
    template_name = 'base.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'

class BootView(TemplateView):
    template_name = 'boot.html'

class ClientesView(TemplateView):
    template_name = 'padrao/form.html'
