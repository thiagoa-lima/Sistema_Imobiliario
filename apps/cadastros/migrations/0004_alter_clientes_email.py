# Generated by Django 4.1.6 on 2023-03-06 18:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_rename_telefone_1_clientes_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='teste'), blank=True, null=True, size=8),
        ),
    ]
