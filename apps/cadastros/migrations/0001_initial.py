# Generated by Django 4.1.6 on 2023-03-06 18:22

import cpf_field.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('tipo_cliente', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tipo')),
                ('cep', models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP')),
                ('endereco', models.CharField(blank=True, max_length=200, null=True, verbose_name='Endereço')),
                ('numero', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('uf', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), blank=True, size=None)),
                ('email_1', models.EmailField(blank=True, max_length=50, null=True, verbose_name='E-mail (1)')),
                ('email_2', models.EmailField(blank=True, max_length=50, null=True, verbose_name='E-mail (2)')),
                ('telefone_1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('telefone_2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('telefone_3', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Clientes',
                'verbose_name_plural': 'Clientes',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Imoveis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Casa', 'Casa'), ('Apartamento', 'Apartamento'), ('Sala comercial', 'Sala comercial')], max_length=20, verbose_name='Tipo de Imóvel')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('endereco', models.CharField(default=None, max_length=200, verbose_name='Endereço')),
                ('numero', models.CharField(default=None, max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(default=None, max_length=100, verbose_name='Cidade')),
                ('uf', models.CharField(default=None, max_length=2, verbose_name='UF')),
                ('taxa_admin_mensal', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tx Adm Mensal (%)')),
                ('taxa_admin_anual', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tx Adm Anual (%)')),
                ('repasse_garantido', models.CharField(choices=[('Não possui', 'Não possui'), ('Todo contrato', 'Garantir por todo contrato')], default=None, max_length=100, verbose_name='Repasse Garantido')),
                ('regra_do_repasse', models.CharField(choices=[('DIAS CORRIDOS', 'Dias corridos após o vencimento do aluguel')], default=None, max_length=100, verbose_name='Regra do repasse')),
                ('dias_para_repasse', models.IntegerField(blank=True, default=5, null=True, verbose_name='Dias para repasse')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cliente_proprietario', to='cadastros.clientes', verbose_name='Proprietário')),
            ],
            options={
                'verbose_name': 'Imóvel',
                'verbose_name_plural': 'Imóveis',
            },
        ),
        migrations.CreateModel(
            name='ClientePF',
            fields=[
                ('clientes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastros.clientes')),
                ('cpf', cpf_field.models.CPFField(blank=True, max_length=14, null=True, unique=True, verbose_name='CPF')),
                ('pai', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome do pai')),
                ('mae', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome da mãe')),
                ('rg', models.CharField(blank=True, max_length=20, verbose_name='RG')),
                ('orgao_expedidor', models.CharField(blank=True, max_length=20, null=True, verbose_name='Orgão Expedidor')),
                ('data_expedicao', models.DateField(blank=True, max_length=10, null=True, verbose_name='Data de Expedição')),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True, verbose_name='Sexo')),
                ('nascimento', models.DateField(blank=True, max_length=10, null=True, verbose_name='Nascimento')),
                ('estado_civil', models.IntegerField(blank=True, choices=[(1, 'Casado(a)'), (2, 'Divorciado(a)'), (3, 'Solteiro(a)'), (4, 'União Estável'), (5, 'Viúvo(a)')], null=True, verbose_name='Estado Civil')),
                ('nacionalidade', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nacionalidade')),
                ('naturalidade', models.CharField(blank=True, max_length=50, null=True, verbose_name='Naturalidade')),
                ('nome_conjunge', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome Completo')),
                ('cpf_conjuge', cpf_field.models.CPFField(blank=True, max_length=14, null=True, verbose_name='CPF')),
                ('rg_conjuge', models.CharField(blank=True, max_length=20, null=True, verbose_name='RG')),
                ('orgao_expedidor_conjuge', models.CharField(blank=True, max_length=20, null=True, verbose_name='Orgão Expedidor')),
                ('data_expedicao_conjuge', models.DateField(blank=True, max_length=10, null=True, verbose_name='Data de Expedição')),
                ('sexo_conjuge', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True, verbose_name='Sexo')),
                ('profissao_conjuge', models.CharField(blank=True, max_length=20, null=True, verbose_name='Profissão')),
                ('telefone_conjuge', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone Comercial')),
                ('celular_conjuge', models.CharField(blank=True, max_length=15, null=True, verbose_name='Celular')),
                ('email_conjuge', models.EmailField(blank=True, max_length=50, null=True, verbose_name='E-mail')),
            ],
            bases=('cadastros.clientes',),
        ),
        migrations.CreateModel(
            name='Saida_de_Chaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_retirada', models.DateField(default=None, verbose_name='Data')),
                ('hora_retirada', models.TimeField(default=None, verbose_name='Hora')),
                ('data_devolucao', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('hora_devolucao', models.TimeField(blank=True, null=True, verbose_name='Hora')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('cliente', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cliente', to='cadastros.clientes', verbose_name='Cliente')),
                ('imovel', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Imovel +', to='cadastros.imoveis', verbose_name='imovel')),
            ],
        ),
        migrations.CreateModel(
            name='ClientePJ',
            fields=[
                ('clientes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastros.clientes')),
                ('cnpj', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='CNPJ')),
                ('nome_fantasia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome fantasia')),
                ('inscricao_estadual', models.CharField(blank=True, max_length=20, null=True, verbose_name='Inscrição estadual')),
                ('data_abertura', models.DateField(blank=True, max_length=10, null=True, verbose_name='Data de abertura')),
                ('situacao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Situação')),
                ('data_situacao', models.DateField(blank=True, max_length=10, null=True, verbose_name='Data da situação')),
                ('porte', models.CharField(blank=True, max_length=50, null=True, verbose_name='Porte')),
                ('natureza_juridica', models.CharField(blank=True, max_length=50, null=True, verbose_name='Natureza Jurídica')),
                ('tipo_responsavel_1', models.CharField(blank=True, choices=[('Sócio', 'Sócio'), ('Procurador', 'Procurador')], max_length=20, null=True, verbose_name='Tipo')),
                ('tipo_responsavel_2', models.CharField(blank=True, choices=[('Sócio', 'Sócio'), ('Procurador', 'Procurador')], max_length=20, null=True, verbose_name='Tipo')),
                ('responsavel_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Cliente_PJ_responsavel_1', to='cadastros.clientes', verbose_name='Responsável 1')),
                ('responsavel_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Cliente_PJ_responsavel_2', to='cadastros.clientes', verbose_name='Responsável 2')),
            ],
            bases=('cadastros.clientes',),
        ),
    ]
