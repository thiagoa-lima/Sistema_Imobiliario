from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Administracao, Aluguel, Financeiro_do_Contrato
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from . import forms

def Listar_Financeiro_do_aluguel(request, pk):  
    context = {}
    contratos = Aluguel.objects.filter(id=pk)
    parcelas = Financeiro_do_Contrato.objects.filter(contrato_id=pk)
    context['contratos'] = contratos
    context['parcelas'] = parcelas 
    
    
    
# ----------------------------------------------------------------------------------- 
    num_parcelas = None
    print(num_parcelas)

    if request.method == 'POST':
        num_parcelas = None
        print(num_parcelas)

        num_parcelas = request.POST['num_parcelas']
        primeira_parcela = request.POST['primeira_parcela']
        vencimento_primeira_parcela = request.POST['vencimento_primeira_parcela']
        valor_da_parcela=request.POST['valor_da_parcela']
        print(num_parcelas)

        if num_parcelas != None:
            nova_parcela = Financeiro_do_Contrato.objects.create(
                    parcela=primeira_parcela, 
                    contrato_id=pk,
                    vencimento=vencimento_primeira_parcela,
                    valor=valor_da_parcela,
                    multa=0,
                    juros=0,
                    valor_total=0,
                )
    
    
    
    # if request.method == 'POST':
    #     num_parcelas = None
    #     print(num_parcelas)

    #     num_parcelas = request.POST['num_parcelas']
    #     print(num_parcelas)

    #     if num_parcelas != None:
    #         nova_parcela = Financeiro_do_Contrato.objects.create(
    #                 parcela=num_parcelas, 
    #                 contrato_id=pk,
    #             )



# ----------------------------------------------------------------------------------- 

    return render(request, 'contratos/aluguel/lista_financeiro.html', context)

# @receiver(pre_save, sender=Financeiro_do_Contrato)
# def Calcula_vencimento_real(sender, instance, *args, **kwargs):
#     if datetime.date.weekday(instance.vencimento) == 6:
#         instance.vencimento_real = (instance.vencimento + relativedelta(days=+1))
#     elif datetime.date.weekday(instance.vencimento) == 5:
#         instance.vencimento_real = (instance.vencimento + relativedelta(days=+2))
  


# ===================================================================================
# ------ CREATE ---------------------------------------------------------------------
# ===================================================================================

class AdministracaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Administracao
    form_class = forms.AdministracaoForm
    template_name = 'contratos/administracao/form.html'
    success_url = reverse_lazy('contrato-administracao-listar')

    # O método abaixo serve para alterar os campos dentro dos formulários. Incluir também no form.html
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Novo contrato de administração"
        context['botao'] = "Cadastrar"
        
        return context

class AluguelCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = forms.AluguelForm
    model = Aluguel
    template_name = 'contratos/aluguel/form.html'
    success_url = reverse_lazy('contrato-aluguel-listar')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Novo contrato de aluguel"
        context['botao'] = "Cadastrar"
        
        return context

# ===================================================================================
# ------ DELETE ---------------------------------------------------------------------
# ===================================================================================

class AluguelDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Aluguel
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('contrato-aluguel-listar')


class AdministracaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Administracao
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('contrato-administracao-listar')

# ===================================================================================
# ------ UPDATE ---------------------------------------------------------------------
# ===================================================================================

class AluguelUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Aluguel
    form_class = forms.AluguelForm
    template_name = 'contratos/aluguel/form.html'
    success_url = reverse_lazy('contrato-aluguel-listar')
    
    # Atualizar os campos do formulário
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar contrato de aluguel"
        context['botao'] = "Salvar"
        
        return context

class Financeiro_do_ContratoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    fields = '__all__'
    template_name = 'contratos/financeiro/form.html'

    # Método que guarda o ID do formulário que está sendo atualizado
    def get_success_url(self) -> str:
        return reverse_lazy('financeiro-do-contrato-listar', kwargs={'pk': self.object.pk})

    # Método que atualiza os campos do formulário
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Baixar Parcela de Aluguel"
        context['botao'] = "Baixar Parcela"
        
        return context

# -----------------------------------------------------------------------------------

class AdministracaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Administracao
    form_class = forms.AdministracaoForm
    template_name = 'contratos/administracao/form.html'
    success_url = reverse_lazy('contrato-administracao-listar')

    # Atualizar os campos do formulário
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar contrato de administração"
        context['botao'] = "Salvar"
        
        return context

# -----------------------------------------------------------------------------------



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

class Financeiro_do_ContratoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    template_name = 'contratos/financeiro/lista.html'
   





