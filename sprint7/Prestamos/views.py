from django.shortcuts import render
from .forms import PrestamoForm

# Create your views here.
def formularios(request):
    usuario_nombre = "Armando Esteban Quito"
    prestamo_form = PrestamoForm
    print(prestamo_form.declared_fields)
    return render(request, 'Prestamos/formularios.html', {'usuario_nombre': usuario_nombre, 'prestamo_form': prestamo_form})