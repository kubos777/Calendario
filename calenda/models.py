from django.db import models
# Create your models here.

class Entrada(models.Model):

    nombre =  models.CharField(max_length=100)
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.fechaCreacion}'
