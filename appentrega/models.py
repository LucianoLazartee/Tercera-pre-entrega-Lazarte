from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.comision}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=16)
    apellido = models.CharField(max_length=16)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=16)
    apellido = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} - {self.fecha_entrega} - {self.entregado}"
