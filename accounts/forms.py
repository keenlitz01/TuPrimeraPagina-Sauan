from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False, label='Nombre')
    last_name = forms.CharField(max_length=50, required=False, label='Apellido')
    email = forms.EmailField(required=False, label='Email')

    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email


class CambiarPasswordForm(forms.Form):
    password_actual = forms.CharField(widget=forms.PasswordInput, label='Contraseña actual')
    password_nuevo = forms.CharField(widget=forms.PasswordInput, label='Contraseña nueva')
    password_confirmar = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña nueva')