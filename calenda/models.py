from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Entrada(models.Model):

    nombre =  models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.fechaCreacion}'
