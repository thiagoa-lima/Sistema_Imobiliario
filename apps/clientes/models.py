from django.db import models

class Clientes(models.Model):
    # choices
    sexo_choices = (
        (1, 'Masculino'), 
        (2, 'Feminino'),
    )
    qualificacao_choices = (
        (1, 'Locatário'), 
        (2, 'Proprietário'), 
        (3, 'Fiador'),
    )
    tipo_cliente_choices = (
        (1, 'Pessoa Física'), 
        (2, 'Pessoa Jurídica'),
    )
    estado_civil_choices = (
        (1, 'Casado(a)'), 
        (2, 'Divorciado(a)'), 
        (3, 'Solteiro(a)'), 
        (4, 'Viúvo(a)'),
    )
    
    # informações iniciais
    tipo_cliente = models.IntegerField('Tipo Cliente', choices=tipo_cliente_choices, blank=False, null=False)
    qualificacao = models.IntegerField('Qualificação', choices=qualificacao_choices, blank=False, null=False)

    # informações pessoais
    nome = models.CharField('Nome', max_length=100, null=False, blank=False)
    sexo = models.IntegerField('Sexo', choices=sexo_choices, blank=False, null=False)
    cpf = models.CharField('CPF', max_length=20, blank=True)
    rg = models.CharField('RG', max_length=20, blank=True)
    orgao_expedidor = models.CharField('Orgão Expedidor', max_length=20, blank=True, null=True)
    nascimento_cliente = models.DateField('Nascimento', max_length=10, blank=True)
    naturalidade_cliente = models.CharField('Naturalidade', max_length=50, blank=True)
    nacionalidade_cliente = models.CharField('Nacionalidade', max_length=50, blank=True)
    estado_civil = models.IntegerField('Estado civil', choices=estado_civil_choices, blank=True, null=True)
    pai_cliente = models.CharField('Nome do pai', max_length=120, blank=True)
    mae_cliente = models.CharField('Nome da mãe', max_length=120, blank=True)

    # endereço residencial
    cep = models.CharField('CEP', max_length=10, blank=True)
    endereco = models.CharField('Endereço', max_length=200, blank=True)
    numero = models.CharField('Número', max_length=10, blank=True)
    bairro = models.CharField('Bairro', max_length=50, blank=True)
    cidade = models.CharField('Cidade', max_length=100, blank=True)
    uf = models.CharField('UF', max_length=2, blank=True)

    # dados para contato
    telefone_residencial = models.CharField('Telefone Residencial', max_length=10, blank=True)
    celular = models.CharField('Celular', max_length=11, blank=True)
    email = models.EmailField('E-mail', max_length=50, blank=True)

    

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome
