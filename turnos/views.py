from django.shortcuts import render,redirect
from turnos.models import HorarioTurno
from django.db import IntegrityError
from datetime import time
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ClienteForm, ServicioForm, BuscarTurnoForm
from .models import Cliente, Servicio




def home(request):
    turnos = HorarioTurno.objects.all().order_by("fecha", "hora")
    return render(request, "turnos/index.html", {
        "turnos": turnos,
    })


def inicio(request):
    error = None

    if request.method == "POST":
        try:
            turno = HorarioTurno(
                nombre=request.POST.get("nombre"),
                apellido=request.POST.get("apellido"),
                telefono=request.POST.get("telefono"),
                email=request.POST.get("email"),
                fecha=request.POST.get("fecha"),
                hora=request.POST.get("hora")
            )
            turno.save()
            return redirect("turnos:home")

        except:
            error = "Error al guardar turno"

    
    turnos = HorarioTurno.objects.all().order_by("fecha", "hora")

    return render(request, "turnos/index.html", {
        "turnos": turnos,
        "error": error
    })



def eliminar_turno(request, turno_id):
    turno = get_object_or_404(HorarioTurno, id=turno_id)
    turno.delete()
    return redirect("turnos:home") 

@login_required
def inicio(request):
    error = None
    if request.method == "POST":
        try:
            turno = HorarioTurno(
                nombre=request.POST.get("nombre"),
                apellido=request.POST.get("apellido"),
                telefono=request.POST.get("telefono"),
                email=request.POST.get("email"),
                fecha=request.POST.get("fecha"),
                hora=request.POST.get("hora")
            )
            turno.save()
            return redirect("turnos:home")
        except:
            error = "Error al guardar turno"

    turnos = HorarioTurno.objects.all().order_by("fecha", "hora")
    return render(request, "turnos/index.html", {
        "turnos": turnos,
        "error": error
    })

def eliminar_turno(request, turno_id):
    turno = get_object_or_404(HorarioTurno, id=turno_id)
    turno.delete()
    return redirect("turnos:home")

def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("turnos:home")
    return render(request, "turnos/cliente.html", {"form": form})

def crear_servicio(request):
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("turnos:home")
    return render(request, "turnos/servicio.html", {"form": form})

def buscar_turno(request):
    resultados = []
    if request.GET.get("nombre"):
        resultados = HorarioTurno.objects.filter(
            nombre__icontains=request.GET["nombre"]
        )
    return render(request, "turnos/buscar.html", {"resultados": resultados})

def horarios(request):
    turnos = HorarioTurno.objects.all().order_by("fecha", "hora")
    return render(request, "turnos/horarios.html", {"turnos": turnos})

