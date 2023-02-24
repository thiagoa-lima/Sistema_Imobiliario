from django.db import models

# Create your models here.

class Painel_administrativo(models.Model):
    
    # Dados Cadastrais
    cpf_cnpj = models.CharField("CPF/CNPJ", max_length=100, null=True)
    nome_empresa = models.CharField("Nome da empresa", max_length=100, null=True)
    nome_fantasia = models.CharField("Nome fantasia", max_length=100, null=True)

    # Taxas
    multa = models.DecimalField("Taxa de multa (%)", decimal_places=2, max_digits=5, null=True)
    juros_mensal = models.DecimalField("Taxa de juros mensal (%)", decimal_places=2, max_digits=5, null=True)