# Generated by Django 4.1.6 on 2023-02-19 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0038_alter_clientesssss_pj_responsavel_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='tipo_cliente',
            field=models.CharField(blank=True, choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2, null=True, verbose_name='Tipo Cliente'),
        ),
        migrations.AlterField(
            model_name='clientesssss_pj',
            name='responsavel_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Cliente_PJ_responsavel_1', to='cadastros.clientes', verbose_name='Responsável 1'),
        ),
        migrations.AlterField(
            model_name='clientesssss_pj',
            name='responsavel_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Cliente_PJ_responsavel_2', to='cadastros.clientes', verbose_name='Responsável 2'),
        ),
    ]
