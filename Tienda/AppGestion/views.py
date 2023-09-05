from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Producto

def gestion(request):
    return render(request,'gestion.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto.html', {'object_list': productos})

def buscar_productos(request):
    query = request.GET.get('q')
    productos = Producto.objects.filter(
        Q(nombre__icontains=query)
    )
    return render(request, 'producto.html', {'object_list': productos})

def insertar(request):
    if request.method == 'POST':
        var_id = request.POST['id']
        var_nombre = request.POST['nombre']
        var_imagen1 = request.POST['imagen1']
        var_precio = float(request.POST['precio'])
        
        producto = Producto(id=var_id,
                            nombre=var_nombre,
                            imagen1=var_imagen1,
                            precio=var_precio)
        producto.save()
        return redirect('productos')
    return render(request, 'insertar.html')

def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/')

def modificar(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.imagen1 = request.POST['imagen1']
        producto.precio = float(request.POST['precio'])
        producto.save()
        return redirect('productos')
    return render(request, 'modificar.html', {'producto': producto})
    