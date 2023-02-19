# Generated by Django 4.1.6 on 2023-02-19 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0030_clientes_delete_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientesssss_PF',
            fields=[
                ('clientes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastros.clientes')),
                ('cpf', models.CharField(blank=True, max_length=20, null=True, verbose_name='CPF')),
            ],
            bases=('cadastros.clientes',),
        ),
    ]
