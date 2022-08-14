from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None: 
            return render(request, 'Login/Login.html')
        else:
            login(request, user)
            return redirect('Index')


    return render(request, 'Login/Login.html')

def logout_view(request):
    logout(request)
    return render(request, 'Login/Login.html')
#Agregar css + imágenes del sprint 1 + js en static de clientes
#En el index llamar a user.cliente.tarjetas.all() y mostrarlas en el div de las tarjetas, lo mismo con cuentas
#En el form de prestamos, en la view despues del submit crear un Prestamo, y asignarle prestamo.type, prestamo.customer_id, etc. y hacer prestamo.save(), validar con user.client.client_type.get()
#if cliente_type == 'BLack' and request.POST['monto'] > 500000 
#Linkear todo en base.html
#Verificar logout
#Hacer la página de inicio
