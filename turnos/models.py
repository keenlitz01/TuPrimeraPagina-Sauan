from django.db import models
from ckeditor.fields import RichTextField

class HorarioTurno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    fecha = models.DateField()
    hora = models.TimeField()
    imagen = models.ImageField(upload_to='turnos/', null=True, blank=True)
    notas = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} / {self.fecha} {self.hora}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, default="Sin apellido")
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(default="Sin descripcion")

    def __str__(self):
        return self.nombre