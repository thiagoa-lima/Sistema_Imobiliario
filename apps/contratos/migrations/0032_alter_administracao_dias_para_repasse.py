# Generated by Django 4.1.5 on 2023-02-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0031_alter_administracao_dias_para_repasse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administracao',
            name='dias_para_repasse',
            field=models.IntegerField(blank=True, default=5, max_length=100, null=True, verbose_name='Dia para repasse'),
        ),
    ]
