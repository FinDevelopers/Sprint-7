from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm 
from .forms import RegistrationForm 
from django.contrib.auth.models import User
from Cuentas.models import Cliente, Cuenta

# Create your views here.
def home(request):
    return render(request, 'Login/Home.html')
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

def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = (RegistrationForm(request.POST))
        if form.is_valid():
            user = User()
            user.username = request.POST.get('username')
            user.password = request.POST.get('password2')
            user.first_name = request.POST.get('name')
            user.last_name = request.POST.get('surname')
            user.email = request.POST.get('mail')
            user.save()

            cliente = Cliente()
            cliente.customer_name = request.POST.get('name')
            cliente.customer_surname = request.POST.get('surname')
            cliente.customer_dni = request.POST.get('customer_dni')
            cliente.dob = request.POST.get('dob')


            
    return render(request, 'Login/registration.html', {'form': form})

def logout_view(request):
    logout(request)
    #Acá se puede crear un template para cuando desloguea
    return redirect('Login')
    
#Agregar css + imágenes del sprint 1 + js en static de clientes
#En el index llamar a user.cliente.tarjetas.all() y mostrarlas en el div de las tarjetas, lo mismo con cuentas
#En el form de prestamos, en la view despues del submit crear un Prestamo, y asignarle prestamo.type, prestamo.customer_id, etc. y hacer prestamo.save(), validar con user.client.client_type.get()
#if cliente_type == 'BLack' and request.POST['monto'] > 500000 
#Linkear todo en base.html
#Verificar logout
#Hacer la página de inicio
