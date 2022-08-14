from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import is_valid_path
from .forms import PrestamoForm
from .models import Prestamo

# Create your views here.
@login_required(login_url='/login/')
def formularios(request):
    usuario_nombre = request.user.get_full_name()
    prestamo_form = PrestamoForm
    if request.method == 'POST':
        prestamo_form = PrestamoForm(request.POST)
        if prestamo_form.is_valid():
            prestamo = Prestamo()
            prestamo.loan_type = request.POST.get('tipo_prestamo')
            prestamo.loan_date = request.POST.get('fecha')
            prestamo.loan_total = request.POST.get('monto')
            prestamo.customer = request.user.cliente
            prestamo.save()
            print(prestamo.loan_type)
    return render(request, 'Prestamos/formularios.html', {'usuario_nombre': usuario_nombre, 'prestamo_form': prestamo_form})