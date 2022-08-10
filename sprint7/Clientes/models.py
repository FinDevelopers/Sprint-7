from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True, null=False)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    def __str__(self):
        return f"{self.branch_name}"

    class Meta:
        managed = False
        db_table = 'sucursal'

class TipoCliente(models.Model):
    clt_id = models.AutoField(primary_key=True, null=False)
    clt_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.clt_name}"

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True,null=False)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch = models.ForeignKey(Sucursal,  on_delete=models.DO_NOTHING)
    a = models.TextField()  # This field type is a guess.
    #client_type =  models.ForeignKey(TipoCliente, on_delete=models.DO_NOTHING)
    
    #user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'Cliente'


    


