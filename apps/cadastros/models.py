from django.db import models


class Clientes(models.Model):

    # choices
    qualificacao_choices = (
        ('1', 'Fiador'), 
        ('2', 'Locatário'),
        ('3', 'Proprietário'),
    )
    sexo_choices = (
        ('M', 'Masculino'), 
        ('F', 'Feminino'),
    )
    tipo_cliente_choices = (
        ('PF', 'Pessoa Física'), 
        ('PJ', 'Pessoa Jurídica'),
    )
    estado_civil_choices = (
        ('1', 'Casado(a)'), 
        ('2', 'Divorciado(a)'), 
        ('3', 'Solteiro(a)'), 
        ('4', 'União Estável'),
        ('5', 'Viúvo(a)')
    )
    
    # INFORMAÇÕES INICIAIS
    cpf = models.CharField('CPF', max_length=20, blank=True)
    nome = models.CharField('Nome Completo', max_length=100, null=False, blank=False)
    tipo_cliente = models.CharField('Tipo Cliente', max_length=2, choices=tipo_cliente_choices, null=False, blank=False)
    qualificacao = models.CharField('Qualificação', max_length=20, choices=qualificacao_choices, null=True, blank=True)

    # CONTATO
    telefone = models.CharField('Telefone', max_length=10, blank=True)
    celular = models.CharField('Celular', max_length=11, blank=True)
    email = models.EmailField('E-mail', max_length=50, null=True, blank=True)

    # FILIAÇÃO
    pai = models.CharField('Nome do pai', max_length=120, blank=True)
    mae = models.CharField('Nome da mãe', max_length=120, blank=True)
    
    # MAIS OPÇÕES
    rg = models.CharField('RG', max_length=20, blank=True)
    orgao_expedidor = models.CharField('Orgão Expedidor', max_length=20, blank=True, null=True)
    data_expedicao = models.DateField('Data de Expedição', max_length=10, blank=True, null=True)
    sexo = models.CharField('Sexo',max_length=1, choices=sexo_choices, null=True, blank=True)
    nascimento = models.DateField('Nascimento', max_length=10, null=True, blank=True)
    estado_civil = models.IntegerField('Estado Civil', choices=estado_civil_choices, null=True, blank=True)
    nacionalidade = models.CharField('Nacionalidade', max_length=50, null=True, blank=True)
    naturalidade = models.CharField('Naturalidade', max_length=50, null=True, blank=True)

    # CÔNJUGE
    nome_conjunge = models.CharField('Nome Completo', max_length=100, null=True, blank=True)
    cpf_conjuge = models.CharField('CPF', max_length=20, null=True, blank=True)
    rg_conjuge = models.CharField('RG', max_length=20, null=True, blank=True)
    orgao_expedidor_conjuge = models.CharField('Orgão Expedidor', max_length=20, null=True, blank=True)
    data_expedicao_conjuge = models.DateField('Data de Expedição', max_length=10, null=True, blank=True)
    sexo_conjuge = models.CharField('Sexo',max_length=1, choices=sexo_choices, null=True, blank=True)
    profissao_conjuge = models.CharField('Profissão', max_length=20, null=True, blank=True)
    telefone_conjuge = models.CharField('Telefone Residencial', max_length=10, null=True, blank=True)
    celular_conjuge = models.CharField('Celular', max_length=11, null=True, blank=True)
    email_conjuge = models.EmailField('E-mail', max_length=50, null=True, blank=True)

    # ENDEREÇO
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=200, null=True, blank=True)
    numero = models.CharField('Número', max_length=10, null=True, blank=True)
    complemento = models.CharField('Número', max_length=10, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=50, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=100, null=True, blank=True)
    uf = models.CharField('UF', max_length=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

class Imoveis(models.Model):
    
    # choices
    tipo_imovel_choices = [
        ('CASA', 'Casa'),
        ('APARTAMENTO', 'Apartamento'),
        ('SALA COMERCIAL', 'Sala comercial'),
    ]

    # dados básicos
    proprietario = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=False, blank=False, verbose_name='Proprietário', related_name='cliente_proprietario', limit_choices_to={'qualificacao':'3'})
    tipo = models.CharField('Tipo de Imóvel', max_length=20, null=False, blank=False, choices=tipo_imovel_choices)
    
    # Endereço do imóvel
    cep = models.CharField('CEP', max_length=8, null=False, blank=False)
    endereco = models.CharField('Endereço', max_length=200, default=None, null=False, blank=False)
    numero = models.CharField('Número', max_length=10, default=None, null=False, blank=False)
    complemento = models.CharField('Complemento', max_length=10, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=50, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=100, default=None, null=False, blank=False)
    uf = models.CharField('UF', max_length=2, default=None, null=False, blank=False)


    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
    
    def __str__(self):
        if self.complemento == None:
            endereco_completo = self.endereco + ', ' + self.numero + ', ' + self.cidade + '/' + self.uf 
        else:
            endereco_completo = self.endereco + ', ' + self.numero + ', ' + self.complemento + ', ' + self.cidade + '/' + self.uf

        return endereco_completo