# Generated by Django 4.1.6 on 2023-02-18 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0023_clientes_cnpj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='cnpj',
        ),
    ]
