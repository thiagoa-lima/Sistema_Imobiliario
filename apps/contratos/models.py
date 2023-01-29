from django.db import models
from apps.cadastros.models import Clientes, Imoveis
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Administracao(models.Model):
    proprietario = models.ForeignKey(Clientes, on_delete=models.PROTECT, default=None, verbose_name='Proprietário', related_name='Clientes_proprietario +', limit_choices_to={'qualificacao':2})
    imovel = ChainedForeignKey(Imoveis, on_delete=models.PROTECT, default=None, chained_field="proprietario", chained_model_field="proprietario", show_all=False, auto_choose=True,sort=True)

    class Meta():
        verbose_name = 'Contrato de Administração'
        verbose_name_plural = 'Contrato de Administração'

    # def __str__(self) -> str:
    #     return self.proprietario
