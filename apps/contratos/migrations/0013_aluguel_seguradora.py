# Generated by Django 4.1.6 on 2023-02-22 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0012_remove_aluguel_apolice_capitalizacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='seguradora',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Seguradora'),
        ),
    ]
