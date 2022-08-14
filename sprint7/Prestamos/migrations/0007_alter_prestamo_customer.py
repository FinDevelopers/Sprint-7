# Generated by Django 4.0.6 on 2022-08-14 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0025_alter_direccion_options'),
        ('Prestamos', '0006_alter_prestamo_options_alter_prestamo_loan_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prestamos', to='Clientes.cliente', verbose_name='cliente'),
        ),
    ]