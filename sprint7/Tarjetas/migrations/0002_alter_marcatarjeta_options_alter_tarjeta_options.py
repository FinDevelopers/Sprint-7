# Generated by Django 4.0.6 on 2022-08-13 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tarjetas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marcatarjeta',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tarjeta',
            options={'managed': True, 'verbose_name': 'Tarjeta'},
        ),
    ]
