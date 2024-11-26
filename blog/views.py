from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Reserva, ImagenCarrusel, MenuItem
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ReservaForm
from django.views.generic import CreateView, ListView
from django.contrib import messages


def index(request):
    index = Post.objects.all()
    return render(request, 'blog/index.html', {'index': index})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

class CrearReserva(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'blog/crear_reserva.html'
    success_url = 'reservas/exito'

class ListaReservas(ListView):
    model = Reserva
    template_name = 'blog/lista_reservas.html'

def galeria(request):
    imagenes = ImagenCarrusel.objects.all()
    return render(request, 'blog/galeria.html', {'imagenes': imagenes})

def contacto(request):
    return render(request, 'blog/contacto.html')

def menu(request):
    categorias = MenuItem.objects.values_list('categoria', flat=True).distinct()
    items = MenuItem.objects.filter(disponible=True)
    return render(request, 'blog/menu.html', {'categorias': categorias, 'items': items})

def historia(request):
    return render(request, 'blog/historia.html')

def reservar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            mesa = reserva.mesa
            mesa.disponible = False
            mesa.save()
            messages.success(request, "Reserva realizada con éxito.")
            return redirect('home')
    else:
        # Filtrar mesas disponibles según el número de personas ingresado
        form = ReservaForm()
    return render(request, 'blog/crear_reserva.html', {'form': form})

def reservas_exito(request):
    return render(request, 'blog/reservas_exito.html')

def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    mesa = reserva.mesa
    mesa.disponible = True
    mesa.save()
    reserva.delete()
    messages.success(request, "Reserva cancelada y mesa liberada.")
    return redirect('home')