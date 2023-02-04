from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio,  name="Inicio"),
    path('buscar/', views.buscar),
    path('articulos', views.articulos, name="Articulos"),
    path('clientes', views.clientes, name="Clientes"),
    path('pedidos', views.pedidos, name="Pedidos"),  

]
