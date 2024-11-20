from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Reserva, ImagenCarrusel
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

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

class CrearReserva(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'blog/crear_reserva.html'
    success_url = '/reservas/'

class ListaReservas(ListView):
    model = Reserva
    template_name = 'blog/lista_reservas.html'

def inicio(request):
    imagenes = ImagenCarrusel.objects.all()
    return render(request, 'blog/inicio.html', {'imagenes': imagenes})