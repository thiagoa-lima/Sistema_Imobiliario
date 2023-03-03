from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Administracao, Aluguel, Financeiro_do_Contrato, Imoveis
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from . import forms
import datetime
from dateutil.relativedelta import relativedelta
from django.utils.dateparse import parse_date

def Contrato_Aluguel_DETALHES(request, pk):  
    context = {}
    contratos = Aluguel.objects.filter(id=pk)
    parcelas = Financeiro_do_Contrato.objects.filter(contrato_id=pk)
    
    context['contratos'] = contratos
    context['parcelas'] = parcelas 

    # Váriavel para conferir os atributos do contrato
    # contrato_todos_os_dados = Aluguel.objects.get(id=pk)
    # print(contrato_todos_os_dados.__dict__)

    # Váriavel para buscar o imóvel do contrato
    imovel = Aluguel.objects.get(id=pk).imovel_id
    print(imovel)
    
    # Váriavel para buscar da classe Imóveis a quantidade de dias para repasse
    dias_para_repasse = Imoveis.objects.get(id=imovel).dias_para_repasse
    dias_para_repasse = int(dias_para_repasse)
    print("")
    print("Quantidade de dias para repasse:  {}".format(dias_para_repasse))
    print("")
 
    if request.method == 'POST':
        num_parcelas = None

        # ----------------------------------------------------------------------------
        # DECLARAÇÃO VARIÁVEIS
        # ----------------------------------------------------------------------------

        num_parcelas_str = request.POST['num_parcelas']
        num_parcelas = int(num_parcelas_str)

        primeira_parcela_str = request.POST['primeira_parcela']
        primeira_parcela = int(primeira_parcela_str)

        vencimento_primeira_parcela_str = request.POST['vencimento_primeira_parcela']
        vencimento_primeira_parcela = parse_date(vencimento_primeira_parcela_str)

        valor_da_parcela_str = request.POST['valor_da_parcela']
        valor_da_parcela = float(valor_da_parcela_str)
        
        taxa_primeira_parcela_str = request.POST['taxa_primeira_parcela']
        taxa_primeira_parcela = float(taxa_primeira_parcela_str)

        taxa_demais_parcelas_str = request.POST['taxa_demais_parcelas']
        taxa_demais_parcelas = float(taxa_demais_parcelas_str)

        comissao_primeira_parcela = valor_da_parcela * taxa_primeira_parcela / 100
        repasse_primeira_parcela = valor_da_parcela - comissao_primeira_parcela

        comissao_demais_parcelas = valor_da_parcela * taxa_demais_parcelas / 100
        repasse_demais_parcelas = valor_da_parcela - comissao_demais_parcelas

        # ----------------------------------------------------------------------------
        # INCLUSÃO DAS NOVAS PARCELAS NO BANCO DE DADOS
        # ----------------------------------------------------------------------------

        for i in range(num_parcelas):
            if num_parcelas != None:

                # --------------------------------------------------------------------
                # VALIDAÇÃO DE DATA PARA CÁLCULO DO VENCIMENTO REAL
                # --------------------------------------------------------------------

                vencimento = (vencimento_primeira_parcela + relativedelta(months=+i))

                vencimento_repasse = (vencimento + relativedelta(days=+dias_para_repasse))

                if datetime.date.weekday(vencimento) == 6:
                    vencimento_real = (vencimento + relativedelta(days=+1))
                elif datetime.date.weekday(vencimento) == 5:
                     vencimento_real = (vencimento + relativedelta(days=+2))
                else:
                    vencimento_real = vencimento
        
                # --------------------------------------------------------------------
                # EFETUA OS LANÇAMENTOS NO BANCO DE DADOS
                # --------------------------------------------------------------------

                if i == 0:
                    nova_parcela = Financeiro_do_Contrato.objects.create(
                            parcela = primeira_parcela + i, 
                            contrato_id = pk,
                            vencimento = vencimento,
                            valor_aluguel = valor_da_parcela,
                            multa = 0,
                            juros = 0,
                            valor_total = valor_da_parcela,
                            vencimento_real = vencimento_real,
                            comissao = comissao_primeira_parcela,
                            valor_repasse = repasse_primeira_parcela,
                            valor_pago = 0,
                            saldo_aluguel = valor_da_parcela,
                            vencimento_repasse = vencimento_repasse,
                            saldo_repasse = repasse_primeira_parcela,
                            valor_repassado = 0
                        )
                else:
                    nova_parcela = Financeiro_do_Contrato.objects.create(
                            parcela = primeira_parcela + i, 
                            contrato_id = pk,
                            vencimento = vencimento,
                            valor_aluguel = valor_da_parcela,
                            multa = 0,
                            juros = 0,
                            valor_total = valor_da_parcela,
                            vencimento_real = vencimento_real,
                            comissao = comissao_demais_parcelas,
                            valor_repasse = repasse_demais_parcelas,
                            valor_pago = 0,
                            saldo_aluguel = valor_da_parcela,
                            vencimento_repasse = vencimento_repasse,
                            saldo_repasse = repasse_primeira_parcela,
                            valor_repassado = 0
                        )

            i += 1

    return render(request, 'contratos/aluguel/detalhes/detalhes.html', context)

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

class AdministracaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Administracao
    form_class = forms.AdministracaoForm
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('contrato-administracao-listar')

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

class AdministracaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Administracao
    template_name = 'contratos/administracao/lista.html'


# ===================================================================================
# ------ RECEITAS - ALUGUEIS --------------------------------------------------------
# ===================================================================================

class Receitas_a_Receber_LIST(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    template_name = 'receitas/a receber/lista.html'

    def get_queryset(self):
        return Financeiro_do_Contrato.objects.filter(valor_pago = 0)
    
class Receitas_a_Receber_UPDATE(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    form_class = forms.Baixa_de_Parcela_Aluguel_Form
    template_name = 'receitas/baixa_de_parcela.html'
    success_url = reverse_lazy('receitas-a-receber-listar')

    # Método que atualiza os campos do formulário
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Baixar Parcela de Aluguel"
        context['botao'] = "Baixar Parcela"
        
        return context

class Receitas_Recebidas_LIST(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    template_name = 'receitas/recebidas/lista.html'

    def get_queryset(self):
        return Financeiro_do_Contrato.objects.filter(saldo_aluguel = 0)

class Receitas_Recebidas_UPDATE(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    form_class = forms.Baixa_de_Parcela_Aluguel_Form
    template_name = 'receitas/baixa_de_parcela.html'
    success_url = reverse_lazy('receitas-recebidas-listar')

    # Método que atualiza os campos do formulário
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Baixar Parcela de Aluguel"
        context['botao'] = "Baixar Parcela"
        
        return context

# ===================================================================================
# ------ FINANCEIRO DO CONTRATO -----------------------------------------------------
# ===================================================================================

class Financeiro_do_Contrato_Aluguel_UPDATE(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    form_class = forms.Baixa_de_Parcela_Aluguel_Form
    template_name = 'contratos/aluguel/detalhes/baixa_de_parcela.html'

    # Método que guarda o ID do formulário que está sendo atualizado
    def get_success_url(self) -> str:
        return reverse_lazy('financeiro-do-contrato-listar', kwargs={'pk': self.object.contrato_id})

    # Método que atualiza os campos do formulário
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Baixar Parcela de Aluguel"
        context['botao'] = "Baixar Parcela"
        
        return context

class Financeiro_do_Contrato_Aluguel_DELETE(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    template_name = 'padrao/form-excluir.html'

    # Método que guarda o ID do formulário que está sendo atualizado
    def get_success_url(self) -> str:
        return reverse_lazy('financeiro-do-contrato-listar', kwargs={'pk': self.object.contrato_id})
    
class Financeiro_do_Contrato_Aluguel_UPDATE(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    form_class = forms.Baixa_de_Parcela_Aluguel_Form
    template_name = 'contratos/aluguel/detalhes/baixa_de_parcela.html'

    # Método que guarda o ID do formulário que está sendo atualizado
    def get_success_url(self) -> str:
        return reverse_lazy('financeiro-do-contrato-listar', kwargs={'pk': self.object.contrato_id})

    # Método que atualiza os campos do formulário
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Baixar Parcela de Aluguel"
        context['botao'] = "Baixar Parcela"
        
        return context

class Financeiro_do_Contrato_Repasse_UPDATE(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    form_class = forms.Baixa_de_Repasse_Aluguel_Form
    template_name = 'contratos/aluguel/detalhes/baixa_de_repasse.html'

    # Método que guarda o ID do formulário que está sendo atualizado
    def get_success_url(self) -> str:
        return reverse_lazy('financeiro-do-contrato-listar', kwargs={'pk': self.object.contrato_id})
    
    # Atualizar os campos do formulário
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Baixar repasse de aluguel"
        context['botao'] = "Salvar"
        
        return context

# ===================================================================================
# ------ DESPESAS REPASSE -----------------------------------------------------------
# ===================================================================================

class Despesas_a_Repassar_LIST(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    template_name = 'despesas/a repassar/lista.html'

    def get_queryset(self):
        return Financeiro_do_Contrato.objects.filter(valor_repassado = 0)


class Despesas_a_Repassar_UPDATE(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    form_class = forms.Baixa_de_Repasse_Aluguel_Form
    template_name = 'contratos/aluguel/detalhes/baixa_de_repasse.html'
    success_url = reverse_lazy('despesas-a-repassar-listar')

    # Método que atualiza os campos do formulário
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Baixar Parcela de Aluguel"
        context['botao'] = "Baixar Parcela"
        
        return context

# ===================================================================================
# ------ CONTRATO DE ALUGUEL --------------------------------------------------------
# ===================================================================================

class Contrato_Aluguel_CREATE(LoginRequiredMixin, CreateView):
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
    
class Contrato_Aluguel_UPDATE(LoginRequiredMixin, UpdateView):
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
    
class Contrato_Aluguel_DELETE(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Aluguel
    template_name = 'padrao/form-excluir.html'
    success_url = reverse_lazy('contrato-aluguel-listar')

class Contrato_Aluguel_LIST(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Aluguel
    template_name = 'contratos/aluguel/lista.html'

class Detalhes_Contrato_Aluguel_LIST(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Financeiro_do_Contrato
    template_name = 'contratos/aluguel/detalhes/detalhes copy.html'

    def get_queryset(self):
        return Financeiro_do_Contrato.objects.filter(contrato_id=self.kwargs['pk']) 


