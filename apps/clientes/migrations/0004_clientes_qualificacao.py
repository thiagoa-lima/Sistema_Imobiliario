# Generated by Django 4.1.5 on 2023-01-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_clientes_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='qualificacao',
            field=models.CharField(default='L', max_length=15, verbose_name='Qualificação'),
        ),
    ]
