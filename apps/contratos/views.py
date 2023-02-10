from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Administracao, Aluguel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

# ===================================================================================
# ------ CREATE ---------------------------------------------------------------------
# ===================================================================================

class AdministracaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Administracao
    template_name = 'contratos/administracao/form.html'
    success_url = reverse_lazy('listar-contratos')
    fields = [
        'proprietario', 'imovel', 'valor_aluguel', 'taxa_admin_mensal', 'taxa_admin_anual', 'data_inicial', 'prazo_contrato', 
        'data_final', 'repasse_garantido', 'regra_do_repasse', 'dias_para_repasse',
    ]

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Novo contrato de administração"
        context['botao'] = "Cadastrar"
        
        return context

class AluguelCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Aluguel
    template_name = 'contratos/aluguel/form.html'
    success_url = reverse_lazy('contrato-aluguel-listar')
    fields = [
        'proprietario', 'locatario', 'garantia', 'imovel', 'finalidade', 'data_inicial', 'data_final',
        'periodo_meses', 'valor_contrato', 
    ]

# ===================================================================================
# ------ DELETE ---------------------------------------------------------------------
# ===================================================================================

class AluguelDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Aluguel
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('contrato-aluguel-listar')

# ===================================================================================
# ------ UPDATE ---------------------------------------------------------------------
# ===================================================================================

class AluguelUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Aluguel
    template_name = 'contratos/aluguel/form.html'
    success_url = reverse_lazy('contrato-aluguel-listar')
    fields = [
        'proprietario', 'locatario', 'garantia', 'imovel', 'finalidade', 'data_inicial', 'data_final',
        'periodo_meses', 'valor_contrato', 
    ]

# ===================================================================================
# ------ LIST -----------------------------------------------------------------------
# ===================================================================================

class AdministracaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Administracao
    template_name = 'contratos/administracao/lista.html'

class AluguelList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Aluguel
    template_name = 'contratos/aluguel/lista.html'
