from django.db import models

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
    imagen = models.ImageField(upload_to='menu/', blank=True, null=True)

    def __str__(self):
        return self.nombre