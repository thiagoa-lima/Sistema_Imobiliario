# Generated by Django 4.1.6 on 2023-02-22 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0008_aluguel_valor_caucao_alter_aluguel_garantia'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='observacao_garantia',
            field=models.TextField(blank=True, null=True, verbose_name='Observação'),
        ),
    ]
