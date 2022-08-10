from django.shortcuts import render, redirect
from .models import Tarjeta
# Create your views here.
def tarjeta(request):
    if request.user.is_authenticated:
        usuario_nombre = request.user.get_full_name()
        tarjetas = Tarjeta.objects.all().filter(card_customer=7)
        return render(request, 'Tarjetas/tarjeta.html', {"usuario_nombre": usuario_nombre, "tarjetas": tarjetas})
    else:
        return redirect('Login')