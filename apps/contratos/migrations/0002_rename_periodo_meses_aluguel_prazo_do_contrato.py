# Generated by Django 4.1.6 on 2023-02-22 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluguel',
            old_name='periodo_meses',
            new_name='prazo_do_contrato',
        ),
    ]
