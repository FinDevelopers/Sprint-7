from tabnanny import verbose
from django.db import models

# Create your models here.
class TipoCuenta(models.Model):
    act_id = models.AutoField(primary_key=True, verbose_name='ID')
    act_name = models.TextField(blank=True, null=True, verbose_name='nombre')

    def __str__(self):
        return self.act_name

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
        verbose_name = 'Tipo de Cuenta'
        verbose_name_plural = 'Tipos de Cuenta'
        ordering = ['act_id']


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True, verbose_name='ID')
    customer_id = models.IntegerField()
    account_type = models.ForeignKey('TipoCuenta', models.DO_NOTHING, db_column='account_type')
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'