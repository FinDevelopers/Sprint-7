# Generated by Django 4.0.6 on 2022-08-13 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0002_alter_tipocuenta_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuenta',
            options={'managed': False, 'ordering': ['account_id'], 'verbose_name': 'Cuenta', 'verbose_name_plural': 'Cuentas'},
        ),
         migrations.RenameField(
        model_name='cuenta',
        old_name='customer_id',
        new_name='customer',
        ),
    ]
