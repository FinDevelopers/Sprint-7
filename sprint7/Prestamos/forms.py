from django import forms

class PrestamoForm(forms.Form):
    tipo_prestamo = forms.ChoiceField(choices=[('', 'Seleccione una opción'), ('personal', 'Personal'), ('hipoteca', 'Hipoteca'), ('empresa','Empresa')], required=True)
    fecha = forms.DateField(label="fecha", required=True)
    monto = forms.DecimalField(label="monto", required=True)