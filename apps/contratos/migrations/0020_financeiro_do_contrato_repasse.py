# Generated by Django 4.1.6 on 2023-02-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0019_financeiro_do_contrato_comissao'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeiro_do_contrato',
            name='repasse',
            field=models.FloatField(blank=True, null=True, verbose_name='Comissão'),
        ),
    ]
