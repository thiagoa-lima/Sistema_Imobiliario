# Generated by Django 4.1.6 on 2023-02-22 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_alter_clientepj_nome_fantasia'),
        ('contratos', '0003_rename_prazo_do_contrato_aluguel_prazo_contrato'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='fiador',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='Clientes_Fiador +', to='cadastros.clientes', verbose_name='Fiador'),
        ),
    ]
