from django import forms
 
class clientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    direccion = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=14)


class articulosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    nuevo = forms.BooleanField(required=False)
    precio = forms.IntegerField()


class pedidosFormulario(forms.Form):
    IDdePedido = forms.IntegerField()
    fecha = forms.DateField()
    entregado = forms.BooleanField()