from django.contrib import admin

# Register your models here.
from AppCoder.models import Clientes,Pedidos,Articulos

admin.site.register(Clientes)
admin.site.register(Pedidos)
admin.site.register(Articulos)
