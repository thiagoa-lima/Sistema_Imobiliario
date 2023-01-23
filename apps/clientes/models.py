from django.db import models

class Clientes(models.Model):
    sexo_choices = (('M', 'Masculino'), ('F', 'Feminino'), ('Indef', 'Não quero informar'))

    nome = models.CharField('Nome', max_length=120)
    sexo = models.CharField('Sexo', max_length=10, choices=sexo_choices, default='Indef')
    email = models.EmailField('E-mail', max_length=50)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome
