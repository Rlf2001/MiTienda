from django.urls import path
from AppCarrito.views import tienda,agregar_producto,sacar_producto,limpiar_carrito

urlpatterns = [
    path('', tienda,name='tienda'),
    path('agregar/<int:prod_id>', agregar_producto,name='agregar'),
    path('sacar/<int:prod_id>/', sacar_producto, name='sacar'),
    path('limpiar/', limpiar_carrito, name='limpiar'),
]
