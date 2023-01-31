from django.db import models
from apps.cadastros.models import Clientes, Imoveis
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import *

# Módulos importados para alteração automática de datas
from dateutil.relativedelta import relativedelta
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Administracao(models.Model):

    # Choices
    repasse_garantido_choices = (
        ('NAO POSSUI', 'Não possui'), 
        ('TODO CONTRATO', 'Garantir por todo contrato'),
    )
    dia_do_repasse_choices = (
        ('DIAS UTEIS', 'Dias úteis após o vencimento do aluguel') ,
        ('DIAS CORRIDOS', 'Dias corridos após o vencimento do aluguel') ,
    )

    # Dados iniciais
    proprietario = models.ForeignKey(Clientes, on_delete=models.PROTECT, default=None, verbose_name='Proprietário', related_name='Clientes_proprietario +', limit_choices_to={'qualificacao':'3'})
    imovel = ChainedForeignKey(Imoveis, on_delete=models.PROTECT, default=None, chained_field="proprietario", chained_model_field="proprietario", show_all=False, auto_choose=True,sort=True)
    prazo_locacao = models.IntegerField("Prazo de Aluguel", default=36,validators=[MinValueValidator(0)])
    valor_aluguel = models.IntegerField("Valor do aluguel", default=0,validators=[MinValueValidator(0)])
    taxa_admin_mensal = models.DecimalField("Tx Adm Mensal", decimal_places=2, max_digits=5, default=10,validators=[MinValueValidator(0), MaxValueValidator(100)])
    taxa_admin_anual = models.DecimalField("Tx Adm Anual", decimal_places=2, max_digits=5, default=50,validators=[MinValueValidator(0), MaxValueValidator(100)])
    data_inicial = models.DateField("Data Inicial", max_length=10, null=False, blank=False, default=None)
    data_final = models.DateField("Data Final", max_length=10, null=False, blank=False, default=None)
    

    # Dados do repasse
    repasse_garantido = models.CharField("Repasse Garantido", max_length=100, default=None, choices=repasse_garantido_choices, null=False, blank=False)
    dia_do_repasse = models.CharField("Dia do repasse", max_length=100, default=None, choices=dia_do_repasse_choices, null=False, blank=False)
    dias_para_repasse = models.IntegerField

    class Meta():
        verbose_name = 'Contrato de Administração'
        verbose_name_plural = 'Contrato de Administração'

    def __str__(self) -> str:
        endereco = str(self.imovel)
        return endereco
        
@receiver(pre_save, sender=Imoveis)
def callback_Administracao(sender, instance, *args, **kwargs):
    instance.data_final = (instance.data_inicial + relativedelta(months=+1))
