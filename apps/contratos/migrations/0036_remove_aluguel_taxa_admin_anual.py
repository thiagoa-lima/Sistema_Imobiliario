# Generated by Django 4.1.6 on 2023-03-02 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0035_alter_aluguel_taxa_admin_anual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluguel',
            name='taxa_admin_anual',
        ),
    ]
