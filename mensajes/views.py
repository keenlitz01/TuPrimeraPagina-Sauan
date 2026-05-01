from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Mensaje

@login_required
def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'mensajes/bandeja_entrada.html', {'mensajes': mensajes_recibidos})

@login_required
def mensajes_enviados(request):
    enviados = Mensaje.objects.filter(remitente=request.user)
    return render(request, 'mensajes/mensajes_enviados.html', {'mensajes': enviados})

@login_required
def enviar_mensaje(request):
    usuarios = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        destinatario_id = request.POST.get('destinatario')
        asunto = request.POST.get('asunto')
        contenido = request.POST.get('contenido')
        if destinatario_id and asunto and contenido:
            destinatario = get_object_or_404(User, id=destinatario_id)
            Mensaje.objects.create(
                remitente=request.user,
                destinatario=destinatario,
                asunto=asunto,
                contenido=contenido
            )
            messages.success(request, 'Mensaje enviado correctamente')
            return redirect('mensajes:bandeja_entrada')
        else:
            messages.error(request, 'Completá todos los campos')
    return render(request, 'mensajes/enviar_mensaje.html', {'usuarios': usuarios})

@login_required
def detalle_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, id=mensaje_id)
    if mensaje.destinatario == request.user and not mensaje.leido:
        mensaje.leido = True
        mensaje.save()
    return render(request, 'mensajes/detalle_mensaje.html', {'mensaje': mensaje})