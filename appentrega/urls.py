from django.urls import path
from .views import *

urlpatterns = [
    path("", buscar_comision, name="inicioApp"),
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables"),
    path("busquedaComisiones/", buscando_comision),
]
