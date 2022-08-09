from django.db import models

# Create your models here.
class MarcaTarjeta(models.Model):
    cat_id = models.AutoField(primary_key=True, blank=True)
    cat_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True, blank=True)
    card_brand = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING, db_column='card_brand')
    card_number = models.TextField(unique=True)
    card_cvv = models.IntegerField()
    card_from_date = models.DateTimeField()
    card_expiration_date = models.DateTimeField()
    card_type = models.TextField()
    card_customer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'