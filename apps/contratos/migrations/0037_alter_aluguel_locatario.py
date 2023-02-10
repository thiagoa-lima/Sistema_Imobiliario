# Generated by Django 4.1.5 on 2023-02-10 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0020_alter_clientes_celular_and_more'),
        ('contratos', '0036_alter_aluguel_locatario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='locatario',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='locatario +', to='cadastros.clientes', verbose_name='Locatário'),
        ),
    ]
