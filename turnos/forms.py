from django import forms
from .models import HorarioTurno, Cliente, Servicio

class TurnoForm(forms.ModelForm):
    class Meta:
        model = HorarioTurno
        fields = "__all__"


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"


class BuscarTurnoForm(forms.Form):
    nombre = forms.CharField(max_length=50)