from django.urls import path
from . import views

app_name = 'turnos'

urlpatterns = [
    path('', views.inicio, name='home'),
    path('eliminar/<int:turno_id>/', views.eliminar_turno, name='eliminar_turno'),
    path('cliente/', views.crear_cliente, name='cliente'),
    path('servicio/', views.crear_servicio, name='servicio'),
    path('buscar/', views.buscar_turno, name='buscar'),
    path('horarios/', views.HorariosView.as_view(), name='horarios'),
    path('about/', views.AboutView.as_view(), name='about'),
]
