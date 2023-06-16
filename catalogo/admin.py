from django.contrib import admin
from .models import TipoConfite, Producto

@admin.register(TipoConfite)
class TipoConfiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'tipo')