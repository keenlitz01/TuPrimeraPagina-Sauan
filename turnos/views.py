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

        hora_str = request.POST.get("hora")
        hora_obj = time.fromisoformat(hora_str)

        # 🔒 Validación horario
        if hora_obj < time(9, 0) or hora_obj > time(18, 0):
            error = "Horario fuera de atención (9 a 18 hs)"
        else:
            try:
                turno = HorarioTurno(
                    nombre=request.POST.get("nombre"),
                    apellido=request.POST.get("apellido"),
                    telefono=request.POST.get("telefono"),
                    email=request.POST.get("email"),
                    fecha=request.POST.get("fecha"),
                    hora=hora_str
                )
                turno.save()
                return redirect("base")

            except IntegrityError:
                error = "Ese horario ya está ocupado"

    turnos = HorarioTurno.objects.all().order_by("fecha", "hora")

    return render(request, "turnos/index.html", {
        "turnos": turnos,
        "error": error
    })



def eliminar_turno(request, turno_id):
    turno = get_list_or_404(HorarioTurno, id=turno_id)
    turno.delete()
    return redirect("base") 

