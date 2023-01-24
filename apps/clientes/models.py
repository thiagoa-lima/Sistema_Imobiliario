from django.db import models

class Clientes(models.Model):
    sexo_choices = (('M', 'Masculino'), ('F', 'Feminino'), ('Indef', 'Não quero informar'))
    qualificacao_choices = (('L', 'Locatário'), ('P', 'Proprietário'), ('F', 'Fiador'))
    tipo_cliente_choices = ((1, 'Pessoa Física'), (2, 'Pessoa Jurídica'))
    
    tipo_cliente = models.CharField('Tipo Cliente', max_length=20, choices=tipo_cliente_choices, default=1)
    qualificacao = models.CharField('Qualificação', max_length=15, choices=qualificacao_choices, default="L")
    nome = models.CharField('Nome', max_length=120)
    sexo = models.CharField('Sexo', max_length=10, choices=sexo_choices, default='Indef')
    email = models.EmailField('E-mail', max_length=50)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome
