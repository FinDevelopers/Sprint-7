from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tarjeta
# Create your views here.
@login_required(login_url='/login/')
def tarjeta(request):
    usuario_nombre = request.user.get_full_name()
    tarjetas = Tarjeta.objects.all().filter(card_customer=7)
    return render(request, 'Tarjetas/tarjeta.html', {"usuario_nombre": usuario_nombre, "tarjetas": tarjetas})