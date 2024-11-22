from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Reserva, ImagenCarrusel, MenuItem
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ReservaForm
from django.views.generic import CreateView, ListView


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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
            reserva = form.save(commit=False)
            # Verificar que la mesa tenga capacidad suficiente
            if reserva.num_personas <= reserva.mesa.capacidad:
                # Verificar que la mesa no esté reservada a la misma hora y fecha
                mesas_reservadas = Reserva.objects.filter(
                    fecha=reserva.fecha, hora=reserva.hora, mesa=reserva.mesa
                )
                if not mesas_reservadas:
                    reserva.save()
                    return redirect('reservas_exito')  # Redirige a una página de éxito
                else:
                    form.add_error('mesa', 'Esta mesa ya está reservada para la fecha y hora seleccionadas.')
            else:
                form.add_error('mesa', 'La capacidad de la mesa no es suficiente para el número de personas.')
    else:
        # Filtrar mesas disponibles según el número de personas ingresado
        form = ReservaForm()
    return render(request, 'blog/crear_reserva.html', {'form': form})

def reservas_exito(request):
    return render(request, 'blog/reservas_exito.html')