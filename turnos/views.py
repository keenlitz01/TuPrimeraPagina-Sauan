from django.shortcuts import render,redirect
from turnos.models import HorarioTurno
from django.db import IntegrityError
from datetime import time
from django.shortcuts import get_list_or_404


def home(request):
    return render(request,"turnos/index.html",{"turnos": turnos,})
turnos =True


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
            return redirect("base")

        except:
            error = "Error al guardar turno"

    
    turnos = HorarioTurno.objects.all().order_by("fecha", "hora")

    return render(request, "turnos/index.html", {
        "turnos": turnos,
        "error": error
    })



def eliminar_turno(request, turno_id):
    turno = get_list_or_404(HorarioTurno, id=turno_id)
    turno.delete()
    return redirect("base") 

