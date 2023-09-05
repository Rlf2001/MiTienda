from django.urls import path
from .views import gestion,productos,insertar,eliminar,modificar,buscar_productos

urlpatterns=[
    path("", gestion, name="gestion"),
    path("productos/", productos, name="productos"),
    path("insertar/", insertar, name="insertar"),
    path("eliminar/<int:id>/", eliminar, name="eliminar"),
    path("modificar/<int:id>/", modificar, name="modificar"),
    path('buscar/', buscar_productos, name='buscar_productos'),
]