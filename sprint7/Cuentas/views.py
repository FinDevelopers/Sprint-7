from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cuenta

# Create your views here.
@login_required(login_url='/login/')
def movimientos(request):
    usuario_nombre = request.user.get_full_name()
    #tarjetas = Tarjeta.objects.all().filter(card_customer=7)
    movimientos = request.user.cliente.movimientos.all().order_by('-movement_datetime')
    return render(request, 'Cuentas/movimientos.html', {"usuario_nombre": usuario_nombre, "movimientos": movimientos})