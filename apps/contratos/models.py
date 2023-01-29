from django.db import models
from apps.cadastros.models import Clientes, Imoveis

# Create your models here.

class Administracao(models.Model):
    # nome = models.CharField(max_length=100, default='')
    proprietario = models.ForeignKey(Clientes, on_delete=models.PROTECT, default=None, verbose_name='Proprietário', related_name='Clientes_proprietario +', limit_choices_to={'qualificacao':2})
    # imovel = models.ForeignKey(Imoveis, on_delete=models.PROTECT, default=None, verbose_name='Imóvel', limit_choices_to={'proprietario':proprietario})

    class Meta():
        verbose_name = 'Contrato de Administração'
        verbose_name_plural = 'Contrato de Administração'

    # def __str__(self) -> str:
    #     return self.proprietario
