from django.urls import path
from .views import gestion,insertar,eliminar,modificar,buscar_productos,GestionDetailView,GestionListView
urlpatterns=[
    path("", gestion, name="gestion"),
    path("insertar/", insertar, name="insertar"),
    path("eliminar/<int:id>/", eliminar, name="eliminar"),
    path("modificar/<int:id>/", modificar, name="modificar"),
    path('buscar/', buscar_productos, name='buscar_productos'),
    path('productos',GestionListView.as_view(), name="productos"),
    path('detalle/<int:id>',GestionDetailView.as_view()),
    path('buscar/detalle/<int:id>/', GestionDetailView.as_view(), name='detalle_gestion'),
]