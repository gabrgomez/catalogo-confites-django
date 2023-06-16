from django.forms import ModelForm
from .models import TipoConfite, Producto

#agregar un producto
class CrearProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo','nombre','imagen','precio','fch_elab','fch_vence','tipo')

#agregar un tipo de producto
class crearTipoForm(ModelForm):
    class Meta:
        model = TipoConfite
        fields = '__all__'


