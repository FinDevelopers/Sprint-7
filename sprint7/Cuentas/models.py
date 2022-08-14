from django.db import models
from Clientes.models import Cliente

# Create your models here.
class TipoCuenta(models.Model):
    act_id = models.AutoField(primary_key=True, verbose_name='ID')
    act_name = models.TextField(blank=True, null=True, verbose_name='nombre')

    def __str__(self):
        return self.act_name

    class Meta:
        managed = True
        db_table = 'tipo_cuenta'
        verbose_name = 'Tipo de Cuenta'
        verbose_name_plural = 'Tipos de Cuenta'
        ordering = ['act_id']

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True, verbose_name='ID')
    customer = models.ForeignKey(Cliente, models.CASCADE, verbose_name='cliente', related_name='cuentas')
    account_type = models.ForeignKey('TipoCuenta', models.DO_NOTHING,  db_column='account_type', verbose_name='Tipo de Cuenta', related_name='cuentas')
    balance = models.IntegerField(verbose_name='balance')
    iban = models.TextField(verbose_name='Código Internacional de Cuentas Bancarias')

    def balance_total(self):
        return self.balance / 100

    def balance_con_formato(self):
        if self.balance >= 0:
            return '$' + str(self.balance_total()).replace('.',',')
        else:
            return '-$' + str(-self.balance_total()).replace('.',',')

    def __str__(self):
        return f"Cuenta nro."+str(self.account_id)

    class Meta:
        managed = True
        db_table = 'cuenta'
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['account_id']