from django.urls import path
from . import views

app_name = 'mensajes'

urlpatterns = [
    path('', views.bandeja_entrada, name='bandeja_entrada'),
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('enviados/', views.mensajes_enviados, name='mensajes_enviados'),
    path('<int:mensaje_id>/', views.detalle_mensaje, name='detalle_mensaje'),
]