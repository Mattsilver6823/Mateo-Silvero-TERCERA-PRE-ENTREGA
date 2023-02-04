from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=14)


class Articulos(models.Model):
    nombre = models.CharField(max_length=35)
    nuevo = models.BooleanField()
    precio = models.IntegerField()

class Pedidos(models.Model):
    IDdePedido = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"Id de pedido: {self.IDdePedido} - fecha {self.fecha} - entregado {self.entregado}"