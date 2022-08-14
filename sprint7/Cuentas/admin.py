from django.contrib import admin
from .models import TipoCuenta, Cuenta

# Register your models here.
class TipoCuentaAdmin(admin.ModelAdmin):
    list_display = ['act_id', 'act_name']
    list_display_links = ['act_name']
admin.site.register(TipoCuenta, TipoCuentaAdmin)


class CuentaAdmin(admin.ModelAdmin):
    list_display = ['account_id', 'iban', 'customer', 'account_type','balance_con_formato']
    list_display_links = ['iban']
admin.site.register(Cuenta, CuentaAdmin)

