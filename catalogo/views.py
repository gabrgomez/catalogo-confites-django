from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import django.http as http
from .forms import CrearProductoForm
from .models import Producto

#c-------------------CRUD--------------------------
#-------------------------------
#crear producto
def CrearProducto(request):
    context = dict()
    context['form'] = CrearProductoForm()

    if request.method == 'POST':
        print('datos procesados')
        form = CrearProductoForm(request.POST,request.FILES)
        
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
    return render(request, "catalogo/listar_producto.html",
    {'productos':lista_productos})



#-------------------------------
#eliminar producto
def EliminarProducto(request,codigo):
    #CtgProdCod
    instancia = get_object_or_404(Producto, codigo=codigo)
    if request.method == 'POST':
        instancia.delete()
        return redirect('lista_productos')

    return render(request,'catalogo/eliminar_producto.html', {'productos': instancia})
#-------------------------------
#modificar producto
def ModificarProducto(request,codigo):
    instancia = get_object_or_404(Producto, codigo=codigo)

    form = CrearProductoForm(instance=instancia)

    if request.method == "POST":
        form = CrearProductoForm(request.POST, request.FILES, instance=instancia )
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    else:
        form = CrearProductoForm(instance=instancia)
    return render(request,'catalogo/modificar_producto.html', {'form':form, 'productos': instancia})

#-------------------VISTAS GENERALES--------------------------
def home(request):
    return render(request, 'base.html')

def pagina_api(request):
    return render(request, 'pagina_api.html')

def pagina_cotiza(request):
    return render(request, 'pagina_cotiza.html')

def pagina_dulces(request):
    return render(request, 'pagina_dulces.html')

def pagina_login(request):
    return render(request, 'pagina_login.html')

def pagina_snacks(request):
    return render(request, 'pagina_snacks.html')

def index(request):
    return render(request, 'index.html')


