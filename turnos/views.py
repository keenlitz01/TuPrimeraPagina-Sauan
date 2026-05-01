from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db import IntegrityError
from .forms import ClienteForm, ServicioForm, BuscarTurnoForm
from .models import HorarioTurno, Cliente, Servicio

# CBV con Mixin
class HorariosView(LoginRequiredMixin, View):
    def get(self, request):
        turnos = HorarioTurno.objects.all().order_by('fecha', 'hora')
        return render(request, 'turnos/horarios.html', {'turnos': turnos})

# CBV simple
class AboutView(View):
    def get(self, request):
        return render(request, 'turnos/about.html')

@login_required
def inicio(request):
    error = None
    if request.method == 'POST':
        try:
            turno = HorarioTurno(
                nombre=request.POST.get('nombre'),
                apellido=request.POST.get('apellido'),
                telefono=request.POST.get('telefono'),
                email=request.POST.get('email'),
                fecha=request.POST.get('fecha'),
                hora=request.POST.get('hora'),
                notas=request.POST.get('notas'),
            )
            if request.FILES.get('imagen'):
                turno.imagen = request.FILES['imagen']
            turno.save()
            return redirect('turnos:home')
        except:
            error = 'Error al guardar turno'
    turnos = HorarioTurno.objects.all().order_by('fecha', 'hora')
    return render(request, 'turnos/index.html', {'turnos': turnos, 'error': error})

def eliminar_turno(request, turno_id):
    turno = get_object_or_404(HorarioTurno, id=turno_id)
    turno.delete()
    return redirect('turnos:home')

def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('turnos:home')
    return render(request, 'turnos/cliente.html', {'form': form})

def crear_servicio(request):
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('turnos:home')
    return render(request, 'turnos/servicio.html', {'form': form})

def buscar_turno(request):
    resultados = []
    if request.GET.get('nombre'):
        resultados = HorarioTurno.objects.filter(
            nombre__icontains=request.GET['nombre']
        )
    return render(request, 'turnos/buscar.html', {'resultados': resultados})

def horarios(request):
    turnos = HorarioTurno.objects.all().order_by('fecha', 'hora')
    return render(request, 'turnos/horarios.html', {'turnos': turnos})