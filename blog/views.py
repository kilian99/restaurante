from django.shortcuts import render
from .models import ImagenCarrusel, MenuItem
from django.shortcuts import render


def index(request):
    imagenes = ImagenCarrusel.objects.all()
    return render(request, 'blog/index.html', {'index': index, 'imagenes': imagenes})

def contacto(request):
    return render(request, 'blog/contacto.html')

def menu(request):
    categorias = MenuItem.objects.values_list('categoria', flat=True).distinct()
    items = MenuItem.objects.filter(disponible=True)
    return render(request, 'blog/menu.html', {'categorias': categorias, 'items': items})