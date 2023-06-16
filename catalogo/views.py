from django.shortcuts import render
from django.shortcuts import redirect
import django.http as http
from .forms import CrearProductoForm
from .models import Producto

def home(request):
    return render(request, 'base.html')
#-------------------------------
#crear producto
def CrearProducto(request):
    context = dict()
    context['form'] = CrearProductoForm()

    if request.method == 'POST':
        print('datos procesados')
        form = CrearProductoForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
            return http.HttpResponse('producto guardado')
        else:
            print(form.errors)


    return render(request, 'catalogo/crear_producto.html', context)
#-------------------------------
#listar producto
def ListarProducto(request):
    lista_productos = Producto.objects.all()
    return render(request, 'catalogo/listar_producto.html', {'productos':lista_productos})



#-------------------------------
#eliminar producto
def EliminarProducto(request,codigo):
    #CtgProdCod
    instancia = Producto.objects.get(codigo=codigo)
    instancia.delete()

    return redirect('lista_productos')
#-------------------------------
#modificar producto
def ModificarProducto(request,codigo):
    instancia = Producto.objects.get(codigo=codigo)

    form = CrearProductoForm(instance=instancia)

    if request.method == "POST":
        form = CrearProductoForm(request.POST,instance=instancia )
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request,'catalogo/modificar_producto.html', {'form':form})




