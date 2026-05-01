from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm, EditarPerfilForm, CambiarPasswordForm
from .models import Perfil


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            perfil = Perfil.objects.create(usuario=user)
            login(request, user)
            return redirect('turnos:home')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})



@login_required
def perfil(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    return render(request, 'accounts/perfil.html', {'perfil': perfil})


@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=perfil, user=request.user)
        if form.is_valid():
            form.save()
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, 'Perfil actualizado correctamente')
            return redirect('accounts:perfil')
    else:
        form = EditarPerfilForm(instance=perfil, user=request.user)
    return render(request, 'accounts/editar_perfil.html', {'form': form})


@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = CambiarPasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            if user.check_password(form.cleaned_data['password_actual']):
                if form.cleaned_data['password_nuevo'] == form.cleaned_data['password_confirmar']:
                    user.set_password(form.cleaned_data['password_nuevo'])
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Contraseña cambiada correctamente')
                    return redirect('accounts:perfil')
                else:
                    messages.error(request, 'Las contraseñas nuevas no coinciden')
            else:
                messages.error(request, 'La contraseña actual es incorrecta')
    else:
        form = CambiarPasswordForm()
    return render(request, 'accounts/cambiar_password.html', {'form': form})


