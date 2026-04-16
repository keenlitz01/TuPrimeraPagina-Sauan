from django.urls import path
from turnos.views import *
from .views import inicio

urlpatterns = [
path("",home, name="base"),
path('', inicio, name='home'),
path('eliminar/<int:id>/', eliminar_turno, name='eliminar_turno'),

]