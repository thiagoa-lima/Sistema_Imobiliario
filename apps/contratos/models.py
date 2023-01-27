from django.db import models
from apps.cadastros.models import Clientes, Imoveis

# Create your models here.

class Aluguel():
    pass

class Administracao(models.Model):
    proprietario = models.ForeignKey(Clientes, on_delete=models.PROTECT, default=None, verbose_name='Proprietário', related_name='Clientes.proprietario +', limit_choices_to={'qualificacao': 'PROPRIETARIO'})
    
    
    # imovel = models.ForeignKey(Imoveis, on_delete=models.PROTECT, default=None, verbose_name='Imóvel', related_name='Imoveis.tipo +')
    class Meta():
        verbose_name = 'Contrato de Administração'
        verbose_name_plural = 'Contrato de Administração'
