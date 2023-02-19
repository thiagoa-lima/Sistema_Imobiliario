from django.db import models
from cpf_field.models import CPFField

class Clientes(models.Model):
    class Meta:
        abstract = False
        verbose_name = 'Clientes'
        verbose_name_plural = 'Clientes'

    # ----------------------------------------------------------------------------
    # ------ INÍCIO DOS ATRIBUTOS ------------------------------------------------
    # ----------------------------------------------------------------------------

    nome = models.CharField('Nome', max_length=100, null=True, blank=True)
    tipo_cliente = models.CharField('Tipo', max_length=20, null=True, blank=True)

    # ENDEREÇO
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=200, null=True, blank=True)
    numero = models.CharField('Número', max_length=10, null=True, blank=True)
    complemento = models.CharField('Complemento', max_length=100, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=50, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=100, null=True, blank=True)
    uf = models.CharField('UF', max_length=2, null=True, blank=True)

    # ----------------------------------------------------------------------------
    # ------ FIM DOS ATRIBUTOS ---------------------------------------------------
    # ----------------------------------------------------------------------------

    def __str__(self):

        if self.nome==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.nome

class Clientesssss_PF(Clientes):

    # ----------------------------------------------------------------------------
    # ------ ATRIBUTOS -----------------------------------------------------------
    # ----------------------------------------------------------------------------

    # choices
    sexo_choices = (
        ('M', 'Masculino'), 
        ('F', 'Feminino'),
    )
    estado_civil_choices = (
        (1, 'Casado(a)'), 
        (2, 'Divorciado(a)'), 
        (3, 'Solteiro(a)'), 
        (4, 'União Estável'),
        (5, 'Viúvo(a)')
    )
    
    # INFORMAÇÕES INICIAIS

    cpf = CPFField('CPF', null=True, blank=True)

    # CONTATO
    telefone = models.CharField('Telefone', max_length=15, null=True, blank=True)
    celular = models.CharField('Celular', max_length=15, null=True, blank=True)
    email = models.EmailField('E-mail', max_length=50, null=True, blank=True)

    # FILIAÇÃO
    pai = models.CharField('Nome do pai', max_length=120, null=True, blank=True)
    mae = models.CharField('Nome da mãe', max_length=120, null=True, blank=True)
    
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
    cpf_conjuge = CPFField('CPF', null=True, blank=True)
    rg_conjuge = models.CharField('RG', max_length=20, null=True, blank=True)
    orgao_expedidor_conjuge = models.CharField('Orgão Expedidor', max_length=20, null=True, blank=True)
    data_expedicao_conjuge = models.DateField('Data de Expedição', max_length=10, null=True, blank=True)
    sexo_conjuge = models.CharField('Sexo',max_length=1, choices=sexo_choices, null=True, blank=True)
    profissao_conjuge = models.CharField('Profissão', max_length=20, null=True, blank=True)
    telefone_conjuge = models.CharField('Telefone Comercial', max_length=15, null=True, blank=True)
    celular_conjuge = models.CharField('Celular', max_length=15, null=True, blank=True)
    email_conjuge = models.EmailField('E-mail', max_length=50, null=True, blank=True)

class Clientesssss_PJ(Clientes):

    # DADOS DA EMPRESA
    cnpj = models.CharField('CNPJ', max_length=20, null=True, blank=True)
    nome_fantasia = models.CharField('Nome fantasia', max_length=20, null=True, blank=True)
    inscricao_estadual = models.CharField('Inscrição Estadual', max_length=20, null=True, blank=True)
    data_abertura = models.CharField('Data de abertura', max_length=20, null=True, blank=True)
    
    # CONTATO DA EMPRESA
    email_contato = models.CharField('Email contato', max_length=20, null=True, blank=True)
    telefone_1 = models.CharField('Telefone 1', max_length=20, null=True, blank=True)
    telefone_2 = models.CharField('Telefone 2', max_length=20, null=True, blank=True)
    telefone_3 = models.CharField('Telefone 3', max_length=20, null=True, blank=True)
    responsavel_1 = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Responsável 1', related_name='Cliente_PJ_responsavel_1')
    tipo_responsavel_1 = models.CharField('Tipo', max_length=20, null=True, blank=True)
    responsavel_2 = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Responsável 2', related_name='Cliente_PJ_responsavel_2')
    tipo_responsavel_2 = models.CharField('Tipo', max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.nome)

class Clientes_PF(models.Model):

    # choices
    qualificacao_choices = (
        ('Fiador', 'Fiador'), 
        ('Locatário', 'Locatário'),
        ('Proprietário', 'Proprietário'),
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
        (1, 'Casado(a)'), 
        (2, 'Divorciado(a)'), 
        (3, 'Solteiro(a)'), 
        (4, 'União Estável'),
        (5, 'Viúvo(a)')
    )
    
    # INFORMAÇÕES INICIAIS
    cpf = CPFField('CPF')
    nome = models.CharField('Nome Completo', max_length=100, null=True, blank=True)
    tipo_cliente = models.CharField('Tipo Cliente', max_length=2, choices=tipo_cliente_choices, null=True, blank=True)
    qualificacao = models.CharField('Qualificação', max_length=20, choices=qualificacao_choices, null=True, blank=True)

    # CONTATO
    telefone = models.CharField('Telefone', max_length=15, null=True, blank=True)
    celular = models.CharField('Celular', max_length=15, null=True, blank=True)
    email = models.EmailField('E-mail', max_length=50, null=True, blank=True)

    # FILIAÇÃO
    pai = models.CharField('Nome do pai', max_length=120, null=True, blank=True)
    mae = models.CharField('Nome da mãe', max_length=120, null=True, blank=True)
    
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
    cpf_conjuge = CPFField('CPF')
    rg_conjuge = models.CharField('RG', max_length=20, null=True, blank=True)
    orgao_expedidor_conjuge = models.CharField('Orgão Expedidor', max_length=20, null=True, blank=True)
    data_expedicao_conjuge = models.DateField('Data de Expedição', max_length=10, null=True, blank=True)
    sexo_conjuge = models.CharField('Sexo',max_length=1, choices=sexo_choices, null=True, blank=True)
    profissao_conjuge = models.CharField('Profissão', max_length=20, null=True, blank=True)
    telefone_conjuge = models.CharField('Telefone Comercial', max_length=15, null=True, blank=True)
    celular_conjuge = models.CharField('Celular', max_length=15, null=True, blank=True)
    email_conjuge = models.EmailField('E-mail', max_length=50, null=True, blank=True)

    # ENDEREÇO
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=200, null=True, blank=True)
    numero = models.CharField('Número', max_length=10, null=True, blank=True)
    complemento = models.CharField('Complemento', max_length=100, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=50, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=100, null=True, blank=True)
    uf = models.CharField('UF', max_length=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Cliente PF'
        verbose_name_plural = 'Clientes PF'

    def __str__(self):
        return self.nome

class Clientes_PJ(models.Model):

    # Dados Iniciais
    cnpj = models.CharField('CNPJ', max_length=20, null=True, blank=True)
    razao_social = models.CharField('Razão social', max_length=20, null=True, blank=True)
    nome_fantasia = models.CharField('Nome fantasia', max_length=20, null=True, blank=True)
    inscricao_estadual = models.CharField('Inscrição Estadual', max_length=20, null=True, blank=True)
    data_abertura = models.CharField('Data de abertura', max_length=20, null=True, blank=True)
    
    # Endereço
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=200, null=True, blank=True)
    numero = models.CharField('Número', max_length=10, null=True, blank=True)
    complemento = models.CharField('Complemento', max_length=100, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=50, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=100, null=True, blank=True)
    uf = models.CharField('UF', max_length=2, null=True, blank=True)
    
    # Contato
    email_contato = models.CharField('Email contato', max_length=20, null=True, blank=True)
    telefone_1 = models.CharField('Telefone 1', max_length=20, null=True, blank=True)
    telefone_2 = models.CharField('Telefone 2', max_length=20, null=True, blank=True)
    telefone_3 = models.CharField('Telefone 3', max_length=20, null=True, blank=True)
    responsavel_1 = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=False, blank=False, verbose_name='Responsável 1', related_name='cadastros.Clientes_PJ.responsavel_1+')
    tipo_responsavel_1 = models.CharField('Tipo', max_length=20, null=True, blank=True)
    responsavel_2 = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=False, blank=False, verbose_name='Responsável 2', related_name='cadastros.Clientes_PJ.responsavel_2+')
    tipo_responsavel_2 = models.CharField('Tipo', max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'Cliente PJ'
        verbose_name_plural = 'Clientes PJ'

    def __str__(self):
        return self.razao_social

class Imoveis(models.Model):
    
    # choices
    tipo_imovel_choices = [
        ('Casa', 'Casa'),
        ('Apartamento', 'Apartamento'),
        ('Sala comercial', 'Sala comercial'),
    ]

    # dados básicos
    proprietario = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=False, blank=False, verbose_name='Proprietário', related_name='cliente_proprietario')
    tipo = models.CharField('Tipo de Imóvel', max_length=20, null=False, blank=False, choices=tipo_imovel_choices)
    
    # Endereço do imóvel
    cep = models.CharField('CEP', max_length=9, null=False, blank=False)
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


