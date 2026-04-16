from django.contrib import admin
from .models import HorarioTurno
from .models import HorarioTurno, Cliente, Servicio




@admin.register(HorarioTurno)
class HorarioTurnoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "fecha", "hora")
    list_filter = ("fecha",)
    search_fields = ("nombre", "apellido", "email")
    ordering = ("fecha", "hora")

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email")
    search_fields = ("nombre", "apellido", "email")

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio")
    search_fields = ("nombre", "descripcion")