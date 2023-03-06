# Generated by Django 4.1.6 on 2023-03-06 18:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='tags',
        ),
        migrations.AddField(
            model_name='clientes',
            name='email',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=200, null=True), blank=True, null=True, size=None),
        ),
    ]
