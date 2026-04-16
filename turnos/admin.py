from django.contrib import admin
from .models import HorarioTurno

@admin.register(HorarioTurno)
class HorarioTurnoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "fecha", "hora")
    list_filter = ("fecha",)
    search_fields = ("nombre", "apellido", "email")
    ordering = ("fecha", "hora")
