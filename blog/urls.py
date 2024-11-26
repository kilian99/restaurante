from django.urls import path
from . import views
from .views import CrearReserva, ListaReservas, galeria

urlpatterns = [
    path('', views.index, name='index'),
    path('reservas/crear/', CrearReserva.as_view(), name='crear_reserva'),
    path('reservas/', ListaReservas.as_view(), name='lista_reservas'),
    path('galeria/', galeria, name='galeria'),
    path('contacto/', views.contacto, name='contacto'),
    path('menu/', views.menu, name='menu'),
    path('historia/', views.historia, name='historia'),
    path('reservas/crear/reservas/exito/', views.reservas_exito, name='reservas_exito'),
]