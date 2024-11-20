from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date, time


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
    capacidad = models.IntegerField()

    def __str__(self):
        return f"Mesa {self.numero} (Capacidad: {self.capacidad})"

class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=15)
    fecha = models.DateField(default=date.today)
    hora = models.TimeField(default=time(12,0))
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reserva de {self.nombre_cliente} para el dia {self.fecha} a las {self.hora}"
    
class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to='carrusel/')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo or f"Imagen {self.id}"