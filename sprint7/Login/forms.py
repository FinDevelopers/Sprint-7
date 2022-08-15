from django import forms
from django.contrib.auth.forms import UserCreationForm 

class RegistrationForm(UserCreationForm):
    name = forms.CharField(label="Nombre", max_length=50, required=True)
    surname = forms.CharField(label="Apellido", max_length=50, required=True)
    mail = forms.EmailField(label="Mail", max_length=100, required=True)
    dni = forms.IntegerField(label="DNI", required=True, min_value=0)
    dob = forms.DateField(label="Fecha de Nacimiento", required=True)
    