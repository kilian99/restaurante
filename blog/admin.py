from django.contrib import admin
from .models import Post, Mesa, Reserva, ImagenCarrusel, MenuItem

admin.site.register(Post)

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'fecha','hora', 'mesa')
    list_filter = ('fecha','hora', 'mesa')

@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre',)