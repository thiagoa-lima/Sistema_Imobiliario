from django.db import models
from apps.cadastros.models import Clientes, Imoveis
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import *


# Módulos importados para alteração automática de datas
from dateutil.relativedelta import relativedelta
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Clientes, Imoveis


class Administracao(models.Model):

    # Choices
    repasse_garantido_choices = (
        ('Não possui', 'Não possui'), 
        ('Todo contrato', 'Garantir por todo contrato'),
    )
    dia_do_repasse_choices = (
        ('DIAS UTEIS', 'Dias úteis após o vencimento do aluguel') ,
        ('DIAS CORRIDOS', 'Dias corridos após o vencimento do aluguel') ,
    )

    # Dados iniciais
    proprietario = models.ForeignKey(Clientes, on_delete=models.PROTECT, default=None, verbose_name='Proprietário', related_name='Clientes_proprietario +', limit_choices_to={'qualificacao':'Proprietário'})
    imovel = ChainedForeignKey(Imoveis, on_delete=models.PROTECT, default=None, chained_field="proprietario", chained_model_field="proprietario", show_all=False, auto_choose=True,sort=True)
    valor_aluguel = models.CharField("Valor do aluguel", default=None, max_length=20)
    taxa_admin_mensal = models.CharField("Tx Adm Mensal", default=10, max_length=20)
    taxa_admin_anual = models.CharField("Tx Adm Anual", default=50, max_length=20)
    data_inicial = models.DateField("Data Inicial", max_length=10, null=False, blank=False, default=None)
    prazo_contrato = models.IntegerField("Prazo", default=36,validators=[MinValueValidator(0)])
    data_final = models.DateField("Data Final", max_length=10, null=False, blank=False)
    
    # Dados do repasse
    repasse_garantido = models.CharField("Repasse Garantido", max_length=100, default=None, choices=repasse_garantido_choices, null=False, blank=False)
    regra_do_repasse = models.CharField("Regra do repasse", max_length=100, default=None, choices=dia_do_repasse_choices, null=False, blank=False)
    dias_para_repasse = models.IntegerField("Dias para repasse", default=5, null=True, blank=True)

    class Meta():
        verbose_name = 'Contrato de Administração'
        verbose_name_plural = 'Contrato de Administração'

    def __str__(self) -> str:
        endereco = str(self.imovel)
        return endereco
       
# @receiver(pre_save, sender=Administracao)
# def callback_Administracao(sender, instance, *args, **kwargs):
#     instance.data_final = (instance.data_inicial + relativedelta(months=+3))

class Aluguel(models.Model):

    # Choices
    finalidade_choices = (
        ('Comercial', 'Comercial'),
        ('Industrial', 'Industrial'),
        ('Residencial', 'Residencial'), 
        ('Temporada', 'Temporada'), 
    )

    garantia_choices =(
        ('Caução','Caução'),
        ('Fiador','Fiador'),
        ('Seguro fiança', 'Seguro fiança',),
        ('Título de capitalização', 'Título de capitalização'),
        ('Não possui', 'Não possui'),
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
    proprietario = models.ForeignKey(Clientes, on_delete=models.PROTECT, default=None, verbose_name='Proprietário', related_name='Clientes_proprietario +', limit_choices_to={'qualificacao':'Proprietário'})
    imovel = ChainedForeignKey(Imoveis, on_delete=models.PROTECT, default=None, chained_field="proprietario", chained_model_field="proprietario", show_all=False, auto_choose=True, sort=True)
    garantia = models.CharField('Garantia', max_length=50, choices=garantia_choices, blank=True, null=True)
    locatario = models.ForeignKey(Clientes, on_delete=models.PROTECT, default=None, verbose_name='Locatário', related_name='locatario +', blank=True, null=True, limit_choices_to={'qualificacao':'Locatário'})  
    finalidade = models.CharField('Finalidade', max_length=50, choices=finalidade_choices, blank=True, null=True)
    data_inicial = models.DateField('Data inicial', blank=True, null=True)
    periodo_meses = models.IntegerField('Período (em meses)', blank=True, null=True)
    data_final = models.DateField('Data final', blank=True, null=True)
    valor_contrato = models.CharField('Valor do aluguel', max_length=50, blank=True, null=True)

    # Dados do repasse
    repasse_garantido = models.CharField("Repasse Garantido", max_length=100, default=None, choices=repasse_garantido_choices, null=True, blank=True)
    regra_do_repasse = models.CharField("Regra do repasse", max_length=100, default=None, choices=dia_do_repasse_choices, null=True, blank=True)
    dias_para_repasse = models.IntegerField("Dias para repasse", default=5, null=True, blank=True)

    class Meta():
        verbose_name = 'Contrato de Aluguel'
        verbose_name_plural = 'Contrato de Aluguel'

    def __str__(self):
        imovel = str(self.imovel)
        locatario = str(self.locatario)
        return 'Inquilino: ' + locatario + ', imóvel: ' + imovel
