from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.contratos.models import Aluguel

# Create your models here.
class Fin_Aluguel(models.Model):

    contrato = models.CharField("Contrato", max_length=10, null=True, blank=True)
    vencimento = models.DateField("Vencimento", max_length=10, null=True, blank=True)
    parcela = models.CharField("Parcela", max_length=10, null=True, blank=True)
    valor = models.CharField("Valor", max_length=10, null=True, blank=True)
    multa = models.CharField("Multa", max_length=10, null=True, blank=True)
    juros = models.CharField("Juros", max_length=10, null=True, blank=True)
    valor_total = models.CharField("Valor Total", max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'Aluguel'
        verbose_name_plural = 'Alugueis'
