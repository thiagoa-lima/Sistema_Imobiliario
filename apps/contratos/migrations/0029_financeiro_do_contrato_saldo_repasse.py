# Generated by Django 4.1.6 on 2023-02-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0028_financeiro_do_contrato_valor_repassado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeiro_do_contrato',
            name='saldo_repasse',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Valor repassado'),
        ),
    ]
