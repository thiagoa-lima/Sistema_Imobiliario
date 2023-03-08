# Generated by Django 4.1.6 on 2023-03-07 17:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_alter_clientes_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='imoveis',
            name='data_final',
            field=models.DateField(blank=True, max_length=10, null=True, verbose_name='Data Final'),
        ),
        migrations.AddField(
            model_name='imoveis',
            name='data_inicial',
            field=models.DateField(blank=True, default=None, max_length=10, null=True, verbose_name='Data Inicial'),
        ),
        migrations.AddField(
            model_name='imoveis',
            name='prazo_contrato',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Prazo'),
        ),
        migrations.AddField(
            model_name='imoveis',
            name='valor_aluguel',
            field=models.CharField(default=None, max_length=20, verbose_name='Valor do aluguel'),
        ),
    ]
