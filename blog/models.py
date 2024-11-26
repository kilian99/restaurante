from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date, time
from django.utils.timezone import now


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Mesa {self.numero} - {'Disponible' if self.disponible else 'Reservada'}"

class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=15)
    fecha = models.DateField(default=date.today)
    hora = models.TimeField(default=time(12,0))
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True, null=True)
    num_personas = models.IntegerField(default=1)

    def __str__(self):
        return f"Reserva de {self.nombre_cliente} para el dia {self.fecha} a las {self.hora}"
    
    def liberar_mesa(self):
        if self.fecha < now().date() or (self.fecha == now().date() and self.hora < now().time()):
            self.mesa.disponible = True
            self.mesa.save()
            
    
class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to='carrusel/')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo or f"Imagen {self.id}"
    
class MenuItem(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=[
        ('Entrantes', 'Entrantes'),
        ('Plato Principal', 'Plato Principal'),
        ('Postres', 'Postres'),
        ('Bebidas', 'Bebidas'),
    ])
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre