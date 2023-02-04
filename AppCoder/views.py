from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import clientesFormulario, articulosFormulario, pedidosFormulario
from AppCoder.models import Clientes,Articulos,Pedidos
# Create your views here.





def clientes(request):
 
      if request.method == "POST":
 
            miFormulario = clientesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  cliente = Clientes(nombre=informacion["nombre"], direccion=informacion["direccion"],email=informacion["email"], telefono=informacion["telefono"])
                  cliente.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = clientesFormulario()
 
      return render(request, "AppCoder/clientes.html", {"miFormulario": miFormulario})



def articulos(request):
 
      if request.method == "POST":
 
            miFormulario = articulosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  articulo = Articulos(nombre=informacion["nombre"], nuevo=informacion["nuevo"],precio=informacion["precio"])
                  articulo.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = articulosFormulario()
 
      return render(request, "AppCoder/articulos.html", {"miFormulario": miFormulario})





def pedidos(request):
 
      if request.method == "POST":
 
            miFormulario = pedidosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  pedido = Pedidos(IDdePedido=informacion["IDdePedido"], fecha=informacion["fecha"],entregado=informacion["entregado"])
                  pedido.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = pedidosFormulario()
 
      return render(request, "AppCoder/pedidos.html", {"miFormulario": miFormulario})


def inicio(request):
      return render(request,"AppCoder/inicio.html")


def buscar(request):
#respuesta = f"Estoy buscando el pedido numero: {request.GET['IDdePedido']}"
      if request.GET["IDdePedido"]:
            IDdePedido = request.GET["IDdePedido"]
            pedidos = Pedidos.objects.filter(IDdePedido__icontains = IDdePedido)

            return render(request, "AppCoder/inicio.html", {"pedidos" : pedidos, "IDdePedido" : IDdePedido})

      
      else: 

	      return  "No enviaste datos"
