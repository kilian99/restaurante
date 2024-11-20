from django.urls import path
from . import views
from .views import CrearReserva, ListaReservas, inicio

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('reservas/crear/', CrearReserva.as_view(), name='crear_reserva'),
    path('reservas/', ListaReservas.as_view(), name='lista_reservas'),
    path('inicio/', inicio, name='inicio'),
]