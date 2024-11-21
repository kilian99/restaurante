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
    success_url = '/reservas/'

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