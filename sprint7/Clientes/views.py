from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente
# Create your views here.
#def index(request):
@login_required(login_url='/login/')
def index(request):
    usuario_nombre = request.user.get_full_name()
   
    return render(request, 'Clientes/index.html', {"usuario_nombre": usuario_nombre})