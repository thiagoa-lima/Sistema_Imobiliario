from django.db import models

# Create your models here.

class Painel_administrativo(models.Model):
    
    # Dados Cadastrais
    cpf_cnpj = models.CharField("CPF/CNPJ", max_length=100, null=True, blank=True)
    nome_empresa = models.CharField("Nome da empresa", max_length=100, null=True, blank=True)
    nome_fantasia = models.CharField("Nome fantasia", max_length=100, null=True, blank=True)

    # Contato
    telefone = models.CharField("Telefone", max_length=20, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    site = models.CharField("Site", max_length=50, null=True, blank=True)

    # Endereço
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=200, null=True, blank=True)
    numero = models.CharField('Número', max_length=10, null=True, blank=True)
    complemento = models.CharField('Complemento', max_length=100, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=50, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=100, null=True, blank=True)
    uf = models.CharField('UF', max_length=2, null=True, blank=True)

    # Taxas
    multa = models.DecimalField("Taxa de multa (%)", decimal_places=2, max_digits=5, null=True, blank=True)
    juros_mensal = models.DecimalField("Taxa de juros mensal (%)", decimal_places=2, max_digits=5, null=True, blank=True)

    def __str__(self) -> str:
        return self.nome_fantasia
        