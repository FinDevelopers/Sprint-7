from django.db import models
from Clientes.models import Cliente

# Create your models here.
class MarcaTarjeta(models.Model):
    cat_id = models.AutoField(primary_key=True, blank=True)
    cat_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'marca_tarjeta'
        verbose_name='Marca Tarjeta'
        verbose_name_plural = 'Marcas Tarjeta'

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True, blank=True)
    brand = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING, db_column='card_brand')
    card_number = models.TextField(unique=True)
    card_cvv = models.IntegerField()
    card_from_date = models.DateTimeField()
    card_expiration_date = models.DateTimeField()
    card_type = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, verbose_name='cliente', related_name='tarjetas')

    class Meta:
        managed = True
        db_table = 'tarjeta'
        verbose_name='Tarjeta'