from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # usada para cadastros
from django.views.generic.list import ListView # usada para fazer listas
from .models import Imoveis, Clientes, ClientePF, ClientePJ, Saida_de_Chaves
from django.urls import reverse_lazy
from . import forms

# CONTROLE DE LOGIN e USÁRIOS
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin 



# ===================================================================================
# ------ PÁGINAS PRINCIPAIS
# ===================================================================================

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'

class BootView(TemplateView):
    template_name = 'boot.html'

# ===================================================================================
# ------ CLIENTES - CLASSE PAI ------------------------------------------------------
# ===================================================================================

class Clientes_List(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Clientes
    template_name = 'cadastros/clientes/lista.html'

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
    form_class = forms.Clientes_PF_Form

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
    model = ClientePJ
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
    model = ClientePJ
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

class Imoveis_List(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Imoveis
    template_name = 'cadastros/imoveis/lista.html'

class Imoveis_Create(LoginRequiredMixin, CreateView):
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
  
class Imoveis_Update(LoginRequiredMixin, UpdateView):
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
    
class Imoveis_Delete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'administrador'
    model = Imoveis
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('listar-imoveis')

# ===================================================================================
# ------ SAÍDA DE CHAVES ------------------------------------------------------------
# ===================================================================================

class Saida_de_Chaves_List(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Saida_de_Chaves
    template_name = 'cadastros/saida_de_chaves/lista.html'

class Saida_de_Chaves_Create(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Saida_de_Chaves
    form_class = forms.Saida_de_Chaves_Form
    template_name = 'cadastros/saida_de_chaves/form.html'
    success_url = reverse_lazy('listar-saida-chaves')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Controle de saída de chaves"
        context['botao'] = "Cadastrar"
        
        return context 

class Saida_de_Chaves_Update(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Saida_de_Chaves
    form_class = forms.Saida_de_Chaves_Form
    template_name = 'cadastros/saida_de_chaves/form.html'
    success_url = reverse_lazy('listar-saida-chaves')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Devolver chaves"
        context['botao'] = "Salvar"
        
        return context 
    
class Saida_de_Chaves_Delete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Saida_de_Chaves
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('listar-saida-chaves')

def Saida_de_Chaves_por_Imovel(request, pk): 
    context = {}
    imoveis = Imoveis.objects.filter(pk=pk)
    chaves = Saida_de_Chaves.objects.filter(imovel_id=pk)
    context['imoveis'] = imoveis
    context['chaves'] = chaves 

    if request.method == 'POST':
        cliente = request.POST['cliente']

        lancamento = Saida_de_Chaves.objects.create(
            imovel_id = pk,
            observacao = cliente,
        )
    
    return render(request, 'cadastros/imoveis/chaves.html', context)