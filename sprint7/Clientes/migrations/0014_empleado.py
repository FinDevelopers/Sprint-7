# Generated by Django 4.0.6 on 2022-08-13 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0013_alter_cliente_options_alter_sucursal_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
    ]
