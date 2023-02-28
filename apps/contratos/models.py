from django.db import models
from apps.cadastros.models import Imoveis, Clientes
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import *
from apps.cadastros.models import Imoveis


# Módulos importados para alteração automática de datas
from dateutil.relativedelta import relativedelta
from django.dispatch import receiver

class Administracao(models.Model):

    # Dados iniciais
    proprietario = models.ForeignKey(Clientes, on_delete=models.PROTECT, default=None, verbose_name='Proprietário', related_name='Clientes_proprietario +')
    imovel = ChainedForeignKey(Imoveis, on_delete=models.PROTECT, default=None, chained_field="proprietario", chained_model_field="proprietario", show_all=False, auto_choose=True,sort=True)
    valor_aluguel = models.CharField("Valor do aluguel", default=None, max_length=20)
    taxa_admin_mensal = models.CharField("Tx Adm Mensal", default=10, max_length=20)
    taxa_admin_anual = models.CharField("Tx Adm Anual", default=50, max_length=20)
    data_inicial = models.DateField("Data Inicial", max_length=10, null=False, blank=False, default=None)
    prazo_contrato = models.IntegerField("Prazo", default=36,validators=[MinValueValidator(0)])
    data_final = models.DateField("Data Final", max_length=10, null=False, blank=False)
    
   
    class Meta():
        verbose_name = 'Contrato de Administração'
        verbose_name_plural = 'Contrato de Administração'

    def __str__(self) -> str:
        endereco = str(self.imovel)
        return endereco

class Aluguel(models.Model):

    # Choices
    finalidade_choices = (
        ('Comercial', 'Comercial'),
        ('Industrial', 'Industrial'),
        ('Residencial', 'Residencial'), 
        ('Temporada', 'Temporada'), 
    )

    garantia_choices =(
        ('Não possui', 'Não possui'),
        ('Caução','Caução'),
        ('Fiador','Fiador'),
        ('Seguro fiança', 'Seguro fiança',),
        ('Título de capitalização', 'Título de capitalização'),
    )

    repasse_garantido_choices = (
        ('Não possui', 'Não possui'), 
        ('Todo contrato', 'Garantir por todo contrato'),
    )

    dia_do_repasse_choices = (
        ('DIAS UTEIS', 'Dias úteis após o vencimento do aluguel') ,
        ('DIAS CORRIDOS', 'Dias corridos após o vencimento do aluguel') ,
    )

    # dados do contrato
    proprietario = models.ForeignKey(Clientes, on_delete=models.PROTECT, default=None, verbose_name='Proprietário', related_name='Clientes_proprietario +')
    imovel = ChainedForeignKey(Imoveis, on_delete=models.PROTECT, default=None, chained_field="proprietario", chained_model_field="proprietario", related_name='+', show_all=False, auto_choose=True, sort=True)
    garantia = models.CharField('Garantia', max_length=50, default="Não possui",choices=garantia_choices, blank=False, null=False)
    locatario = models.ForeignKey(Clientes, on_delete=models.PROTECT, default=None, verbose_name='Locatário', related_name='locatario +', blank=True, null=True)  
    finalidade = models.CharField('Finalidade', max_length=50, choices=finalidade_choices, blank=True, null=True)
    data_inicial = models.DateField('Data inicial', blank=True, null=True)
    prazo_contrato = models.IntegerField('Período (em meses)', blank=True, null=True)
    data_final = models.DateField('Data final', blank=True, null=True)
    valor_contrato = models.CharField('Valor do aluguel', max_length=50, blank=True, null=True)
    
    # Garantia - GERAL
    observacao_garantia = models.TextField("Observação", blank=True, null=True)
    data_inicial_garantia = models.DateField('Data inicial', blank=True, null=True)
    data_final_garantia = models.DateField('Data final', blank=True, null=True)

    # Garantia - FIADOR
    fiador = models.ForeignKey(Clientes, on_delete=models.PROTECT, verbose_name='Fiador', related_name='+', null=True, blank=True)

    # Garantia - CAUÇÃO
    valor_garantia = models.CharField('Valor', max_length=50, blank=True, null=True)

    # Garantia - TÍTULO CAPITALIZAÇÃO
    banco_garantia = models.CharField('Banco', max_length=50, blank=True, null=True)
    apolice_garantia = models.CharField('Apólice', max_length=50, blank=True, null=True)
    
    # Garantia - SEGURO FIANÇA
    seguradora = models.CharField('Seguradora', max_length=50, blank=True, null=True)

    # Dados do repasse
    repasse_garantido = models.CharField("Repasse Garantido", max_length=100, default=None, choices=repasse_garantido_choices, null=True, blank=True)
    regra_do_repasse = models.CharField("Regra do repasse", max_length=100, default=None, choices=dia_do_repasse_choices, null=True, blank=True)
    dias_para_repasse = models.IntegerField("Dias para repasse", default=5, null=True, blank=True)
    taxa_admin_mensal = models.CharField("Tx adm mensal (%)", max_length=20, null=True, blank=True)
    taxa_admin_anual = models.CharField("Tx adm anual (%)", max_length=20, null=True, blank=True)


    class Meta():
        verbose_name = 'Contrato de Aluguel'
        verbose_name_plural = 'Contrato de Aluguel'

    def __str__(self):
        locatario = str(self.locatario)
        return locatario
    
class Financeiro_do_Contrato(models.Model):

    parcela = models.DecimalField("Parcela", max_digits=50, decimal_places=0, null=True, blank=True)
    contrato = models.ForeignKey(Aluguel, on_delete=models.PROTECT, verbose_name='Locatário e Imóvel', related_name='contrato +')
    vencimento = models.DateField("Vencimento", max_length=10, null=True, blank=True)
    vencimento_real = models.DateField ("Vencimento real", max_length=20, null=True, blank=True)
    data_pagamento = models.DateField("Data pagamento", null=True, blank=True)
    valor_aluguel = models.DecimalField("Valor do Aluguel", max_digits=50, decimal_places=2, null=True, blank=True)
    multa = models.DecimalField("Multa", max_digits=50, decimal_places=2, null=True, blank=True)
    juros = models.DecimalField("Juros", max_digits=50, decimal_places=2, null=True, blank=True)
    valor_total = models.DecimalField("Valor total", max_digits=50, decimal_places=2, null=True, blank=True)
    valor_pago = models.DecimalField("Valor pago", max_digits=50, decimal_places=2, null=True, blank=True)
    saldo_aluguel = models.DecimalField("Saldo", max_digits=50, decimal_places=2, null=True, blank=True)
    vencimento_repasse = models.DateField("Vcto do repasse", max_length=10, null=True, blank=True)
    data_repasse = models.DateField("Data do repasse", max_length=10, null=True, blank=True)
    comissao = models.DecimalField("Comissão", max_digits=50, decimal_places=2, null=True, blank=True)
    valor_repasse = models.DecimalField("Valor do Repasse",max_digits=50, decimal_places=2, null=True, blank=True)
    valor_repassado = models.DecimalField("Valor repassado", max_digits=50, decimal_places=2, null=True, blank=True)
    saldo_repasse = models.DecimalField("Saldo a repassar", max_digits=50, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Financeiro'
        verbose_name_plural = 'Financeiro do Contrato'

    def __str__(self):
        imovel = str(self.imovel)
        locatario = str(self.locatario)
        return locatario + ': ' + imovel


  