from django.urls import path
from .views import CrearProducto, home, ListarProducto,EliminarProducto, ModificarProducto
urlpatterns = [
    path('agregar', CrearProducto, name='crear_producto'),
    path('lista', ListarProducto,name='lista_productos'),
    path('eliminar/<int:codigo>',EliminarProducto,name='eliminar_producto'),
    path('modificar/<int:codigo>', ModificarProducto, name='modificar_producto'),
]