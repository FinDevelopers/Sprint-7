# Generated by Django 4.0.6 on 2022-08-14 03:45

from django.db import migrations

def actualizar_expiration_date(apps, schema_editor):
    Tarjeta = apps.get_model('Tarjetas','Tarjeta')
    array = ['2026-4-13','2029-7-2','2029-3-1','2030-12-9','2030-2-4','2031-4-21','2028-4-25','2028-11-29','2030-9-30','2030-12-29','2028-4-15','2030-3-24','2030-8-8','2029-12-22','2028-4-26','2029-7-20','2028-11-14','2027-12-28','2028-2-16','2026-8-13','2026-11-18','2030-9-26','2027-6-26','2029-4-8','2029-12-20','2026-5-15','2026-6-23','2030-10-3','2027-2-28','2029-9-21','2029-12-3','2026-5-10','2027-2-13','2026-7-25','2029-2-26','2031-3-25','2028-11-4','2026-4-22','2028-10-20','2026-8-21','2026-11-23','2026-7-27','2029-6-18','2031-3-26','2030-7-12','2031-2-4','2028-7-18','2026-11-14','2027-8-6','2030-2-7','2027-1-20','2030-9-11','2027-12-10','2031-6-30','2030-10-3','2026-10-26','2029-8-29','2029-3-9','2031-8-23','2031-11-29','2030-11-4','2026-7-10','2029-2-23','2027-10-3','2027-8-8','2031-3-10','2029-7-13','2028-11-23','2029-8-6','2027-10-5','2028-2-25','2028-7-15','2027-7-3','2029-1-11','2030-6-16','2031-7-7','2030-11-2','2030-4-22','2027-6-13','2027-11-16','2026-9-17','2029-10-7','2029-5-25','2030-7-21','2031-1-4','2026-4-24','2028-6-2','2030-3-2','2027-2-22','2029-3-29','2028-9-17','2028-4-19','2027-5-7','2028-5-7','2028-3-30','2031-10-1','2029-2-3','2029-10-7','2030-7-8','2026-2-10','2029-3-29','2030-6-25','2028-12-17','2029-12-3','2026-8-2','2027-3-25','2026-4-13','2030-10-24','2030-2-2','2028-11-27','2030-7-13','2030-7-4','2027-8-30','2028-2-3','2028-10-3','2028-5-27','2028-10-27','2030-6-28','2028-2-11','2026-8-13','2030-5-15','2029-5-2','2027-5-16','2031-8-10','2031-4-13','2031-11-19','2030-10-24','2030-2-23','2026-12-4','2029-9-25','2031-2-26','2028-7-25','2031-4-2','2028-2-26','2026-11-1','2030-9-5','2027-7-4','2028-6-27','2029-1-24','2030-5-7','2030-8-16','2028-5-3','2028-6-7','2030-8-4','2028-9-12','2029-3-19','2031-8-9','2028-12-4','2028-3-4','2027-11-28','2029-4-27','2027-4-26','2030-8-10','2027-8-26','2027-7-17','2030-9-10','2030-4-1','2031-6-10','2028-3-8','2030-8-18','2029-7-11','2028-3-18','2027-9-15','2027-11-12','2029-2-6','2028-11-11','2030-6-1','2029-6-25','2029-3-27','2028-3-25','2028-5-15','2031-4-24','2030-11-16','2031-4-12','2027-9-18','2030-4-7','2026-7-14','2027-4-11','2030-9-20','2028-11-13','2027-2-19','2026-12-30','2029-11-26','2029-2-6','2029-2-6','2026-6-23','2029-2-25','2027-8-20','2030-3-26','2030-6-28','2029-11-30','2029-11-1','2027-3-15','2028-5-17','2031-6-27','2028-1-16','2029-8-25','2027-3-7','2027-11-12','2027-3-6','2028-2-28','2029-10-15','2031-6-21','2030-10-15','2027-10-8','2030-10-5','2029-6-12','2029-4-1','2029-6-27','2026-9-21','2027-4-19','2028-6-26','2028-1-14','2028-5-1','2029-8-23','2029-3-10','2031-10-11','2027-4-15','2026-8-8','2030-12-2','2028-11-26','2027-8-12','2030-10-20','2027-8-7','2027-11-16','2031-9-19','2027-12-8','2028-5-18','2030-2-4','2031-10-18','2030-12-2','2026-6-17','2030-12-24','2031-3-7','2031-6-3','2027-1-1','2030-5-21','2029-9-30','2030-3-21','2027-8-26','2029-3-24','2030-7-7','2029-3-7','2031-11-28','2027-11-6','2031-8-12','2027-3-21','2027-9-2','2028-1-23','2031-5-15','2030-7-8','2028-3-4','2027-10-20','2030-4-4','2029-9-25','2029-4-23','2030-2-19','2031-8-2','2029-9-18','2031-5-13','2027-6-21','2031-6-7','2029-11-17','2030-5-10','2029-8-25','2031-12-26','2031-7-6','2031-11-15','2030-2-14','2028-6-26','2028-6-16','2028-3-26','2030-8-13','2028-11-21','2030-3-17','2030-8-9','2027-1-7','2028-4-23','2027-1-22','2027-8-30','2026-7-23','2028-2-28','2030-11-4','2030-9-28','2026-9-12','2030-3-7','2029-7-4','2031-4-13','2026-2-24','2030-7-16','2029-7-14','2030-10-18','2030-12-4','2030-5-19','2027-2-23','2029-7-26','2027-3-22','2027-7-10','2026-8-25','2026-3-6','2031-3-25','2027-10-12','2028-11-18','2030-11-29','2027-1-21','2027-2-13','2030-7-14','2028-3-29','2030-8-22','2028-6-5','2030-1-23','2028-11-29','2027-4-2','2028-8-26','2029-10-12','2027-2-8','2029-3-28','2030-4-2','2029-8-1','2031-10-8','2028-7-24','2030-11-11','2028-8-12','2028-10-29','2031-7-29','2027-8-10','2027-12-20','2031-1-15','2030-2-14','2029-5-11','2031-7-23','2026-9-10','2031-9-6','2027-3-23','2030-6-19','2029-4-12','2028-1-27','2030-7-14','2026-3-17','2028-8-6','2029-2-12','2028-6-25','2030-4-30','2029-5-25','2030-10-6','2031-1-1','2028-7-28','2029-1-4','2030-5-13','2030-9-1','2030-7-9','2026-8-23','2030-2-22','2031-11-9','2031-8-4','2027-11-9','2027-3-13','2028-7-7','2028-4-26','2030-11-8','2030-3-24','2027-10-18','2030-12-20','2026-11-25','2030-5-11','2030-7-15','2027-12-29','2030-4-11','2028-5-20','2029-9-2','2028-2-4','2029-4-21','2028-1-12','2030-7-19','2027-10-21','2028-7-21','2030-1-10','2029-5-28','2028-4-21','2030-1-24','2026-2-4','2031-5-3','2026-2-9','2027-4-18','2029-11-5','2027-3-4','2026-6-15','2028-2-2','2028-7-23','2027-6-16','2029-6-8','2031-6-28','2031-8-18','2027-6-28','2029-7-15','2026-4-2','2031-5-10','2027-11-28','2026-9-7','2028-8-21','2027-5-26','2026-11-20','2030-11-12','2030-7-23','2029-7-26','2028-5-30','2031-7-21','2026-3-19','2027-7-29','2031-9-20','2028-4-7','2029-12-19','2026-7-2','2026-5-23','2029-7-17','2029-5-25','2029-9-2','2028-10-24','2026-12-14','2027-11-14','2029-12-2','2026-7-18','2028-11-20','2030-11-19','2027-7-5','2028-8-2','2030-9-15','2027-8-3','2027-5-11','2031-11-25','2026-11-20','2029-4-8','2028-4-11','2028-7-13','2029-2-5','2026-7-13','2029-5-8','2029-7-29','2031-3-24','2028-10-11','2031-2-24','2030-10-26','2028-12-16','2029-4-2','2030-9-23','2027-4-8','2026-6-14','2030-1-18','2029-8-29','2028-6-28','2031-8-8','2028-10-20','2028-9-28','2029-1-5','2030-9-11','2028-8-4','2028-12-8','2031-9-9','2031-4-23','2026-11-26','2026-3-4','2027-2-24','2028-10-13','2027-10-22','2026-8-7','2028-9-5','2030-2-3','2028-11-6','2031-9-23','2030-11-3','2026-7-10','2030-7-19','2029-6-14','2029-2-17','2026-3-29','2028-7-18','2026-7-28','2029-12-4','2027-6-16','2027-8-28','2029-10-23','2028-9-6','2028-1-15','2027-8-27','2030-6-15','2027-11-14','2030-4-17','2030-10-25','2027-2-3','2028-5-27','2026-4-12','2029-3-28','2028-8-7','2030-4-4','2029-8-4','2030-4-27','2028-5-25','2027-8-17','2029-10-12','2027-5-7']
    i = 0
    for tarjeta in Tarjeta.objects.all().order_by('card_id'):
        tarjeta.card_expiration_date = array[i]
        tarjeta.save()
        i += 1


class Migration(migrations.Migration):

    dependencies = [
        ('Tarjetas', '0011_alter_tarjeta_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarjeta',
            options={'managed': True, 'ordering': ['card_id'], 'verbose_name': 'Tarjeta', 'verbose_name_plural': 'Tarjetas'},
        ),
        migrations.RunPython(actualizar_expiration_date)
    ]
