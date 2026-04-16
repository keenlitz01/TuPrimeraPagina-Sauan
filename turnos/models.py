from django.db import models


class HorarioTurno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    fecha = models.DateField()
    hora = models.TimeField()


class meta:
    unique_together = ("fecha", "hora")



    def __str__(self):
        return f" Turnos: {self.nombre} {self.apellido} / {self.fecha} {self.hora}"
    
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    apellido = models.CharField(max_length=50, default="Sin apellido")
    def __str__(self):
        return self.nombre
    


class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(default="Sin descripcion")

    def __str__(self):
        return self.nombre

