from django.shortcuts import render
from .models import Tarjeta
# Create your views here.
def tarjeta(request):
    usuario_nombre = "Armando Paredes"
    tarjetas = Tarjeta.objects.all().filter(card_customer=7)
    return render(request, 'Tarjetas/tarjeta.html', {"usuario_nombre": usuario_nombre, "tarjetas": tarjetas})