# Generated by Django 4.1.6 on 2023-02-23 14:49

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_alter_clientepj_nome_fantasia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientepf',
            name='cpf',
            field=cpf_field.models.CPFField(blank=True, max_length=14, null=True, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='clientepj',
            name='cnpj',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='CNPJ'),
        ),
    ]
