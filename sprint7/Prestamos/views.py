from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PrestamoForm

# Create your views here.
@login_required(login_url='/login/')
def formularios(request):
    usuario_nombre = request.user.get_full_name()
    prestamo_form = PrestamoForm
    print(prestamo_form.declared_fields)
    return render(request, 'Prestamos/formularios.html', {'usuario_nombre': usuario_nombre, 'prestamo_form': prestamo_form})