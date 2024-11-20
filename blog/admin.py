from django.contrib import admin
from .models import Post, Mesa, Reserva, ImagenCarrusel

admin.site.register(Post)

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'capacidad')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'fecha','hora', 'mesa')
    list_filter = ('fecha','hora', 'mesa')

@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen')