from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse


def cursos(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            curso = Curso(nombre=info["nombre"], comision=info["comision"])
            curso.save()
    else:
        form = CursoForm()

    cursoss = Curso.objects.all()
    contexto = {
        "cursos": cursoss,
        "form": form,
    }
    return render(request, template_name="cursos.html", context=contexto)


def buscar_comision(request):
    return render(request, template_name="inicio.html")


def buscando_comision(request):
    comision = request.GET["comision"]
    if comision != "":
        comisiones = Curso.objects.filter(comision__icontains=comision)
        print(comisiones)
        return render(request, template_name="busquedaComisiones.html", context={"comisiones": comisiones})
    else:
        return render(request, template_name="inicio.html", context={"mensaje": "Por favor, ingrese una "
                                                                                "comisión válida."})


def profesores(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            profesor = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"],
                                profesion=info["profesion"])
            profesor.save()
    else:
        form = ProfesorForm()

    profesoress = Profesor.objects.all()
    contexto = {
        "profesores": profesoress,
        "form": form,
    }
    return render(request, template_name="profesores.html", context=contexto)


def estudiantes(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            estudiante = Estudiante(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
            estudiante.save()
    else:
        form = EstudianteForm()

    estudiantess = Estudiante.objects.all()
    contexto = {
        "estudiantes": estudiantess,
        "form": form,
    }
    return render(request, template_name="estudiantes.html", context=contexto)


def entregables(request):
    if request.method == "POST":
        form = EntregableForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            entregable = Entregable(nombre=info["nombre"], fecha_entrega=info["fecha_entrega"],
                                    entregado=info["entregado"])
            entregable.save()
    else:
        form = EntregableForm()

    entregabless = Entregable.objects.all()
    contexto = {
        "entregables": entregabless,
        "form": form,
    }
    return render(request, template_name="entregables.html", context=contexto)


def inicio(request):
    return HttpResponse("¡Bienvenid@! Para ingresar a la página debe de añadir '/appentrega' al final del enlace.")
