from django.urls import path
from . import views
from .views import CrearReserva, ListaReservas, galeria

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('reservas/crear/', CrearReserva.as_view(), name='crear_reserva'),
    path('reservas/', ListaReservas.as_view(), name='lista_reservas'),
    path('galeria/', galeria, name='galeria'),
    path('contacto/', views.contacto, name='contacto'),
    path('menu/', views.menu, name='menu'),
    path('historia/', views.historia, name='historia'),
    path('reservas/exito/', views.reservas_exito, name='reservas_exito'),
]