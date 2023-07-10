from django import forms
from django.forms import ModelForm
from .models import TipoConfite, Producto

#agregar un producto
class CrearProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo','nombre','imagen','precio','fch_elab','fch_vence','tipo')

        widgets = {
            'fch_elab':forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': "date"},
                format=('%Y-%m-%d'),
                ),
            'fch_vence':forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': "date"},
                format=('%Y-%m-%d'),
                ),
        }
        
#agregar un tipo de producto
class crearTipoForm(ModelForm):
    class Meta:
        model = TipoConfite
        fields = '__all__'


