from django import forms


class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=16)
    apellido = forms.CharField(max_length=16)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)


class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=16)
    apellido = forms.CharField(max_length=16)
    email = forms.EmailField()


class EntregableForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()


class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    comision = forms.IntegerField()
