# Generated by Django 4.1.6 on 2023-02-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0009_aluguel_observacao_garantia'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='apolice_capitalizacao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Valor da caução'),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='banco_capitalizacao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Valor da caução'),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='data_final_garantia',
            field=models.DateField(blank=True, null=True, verbose_name='Data final'),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='data_inicial_garantia',
            field=models.DateField(blank=True, null=True, verbose_name='Data inicial'),
        ),
    ]
