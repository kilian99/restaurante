from django.contrib import admin
from .models import ImagenCarrusel, MenuItem

@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre',)