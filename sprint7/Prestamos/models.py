from tabnanny import verbose
from django.db import models
from Clientes.models import Cliente

# Create your models here.
class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True, blank=True)
    loan_type = models.TextField(choices=[('HIPOTECARIO','Hipotecario'),('PRENDARIO','Prendario'),('PERSONAL','Personal')])
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey(Cliente,  on_delete=models.CASCADE, null=True, blank=True, related_name='prestamos') 

    class Meta:
        managed = True
        db_table = 'prestamo'
        verbose_name = 'Prestamo'
