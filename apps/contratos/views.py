from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Administracao
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# ===================================================================================
# CREATE ('C' - CRUD)
# ===================================================================================

class AdministracaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Administracao
   
    fields = ['proprietario', 'imovel', 'valor_aluguel', 'taxa_admin_mensal', 'taxa_admin_anual', 'data_inicial', 'prazo_contrato', 
        'data_final', 'repasse_garantido', 'regra_do_repasse', 'dias_para_repasse',
    ]
    template_name = 'contratos/administracao/form.html'
    success_url = reverse_lazy('listar-contratos')

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Novo contrato de administração"
        context['botao'] = "Cadastrar"
        
        return context    

# ===================================================================================
# LIST
# ===================================================================================

class AdministracaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Administracao
    template_name = 'contratos/administracao/lista.html'
