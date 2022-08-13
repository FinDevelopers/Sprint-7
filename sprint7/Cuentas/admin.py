from django.contrib import admin
from .models import TipoCuenta

# Register your models here.
class TipoCuentaAdmin(admin.ModelAdmin):
    list_display = ['act_id', 'act_name']
    list_display_links = ['act_name']
admin.site.register(TipoCuenta, TipoCuentaAdmin)


