from django.urls import path
from .views import CrearProducto, home, ListarProducto,EliminarProducto, ModificarProducto,  VerProducto
urlpatterns = [
    path('agregar', CrearProducto, name='crear_producto'),
    path('ver/<str:codigo>', VerProducto, name='ver_producto'),
    path('lista', ListarProducto,name='lista_productos'),
    path('eliminar/<str:codigo>',EliminarProducto,name='eliminar_producto'),
    path('modificar/<str:codigo>', ModificarProducto, name='modificar_producto'),
]