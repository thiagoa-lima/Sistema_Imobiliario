# Generated by Django 4.1.6 on 2023-03-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0034_alter_aluguel_taxa_admin_anual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='taxa_admin_anual',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tx adm anual (%)'),
        ),
    ]
