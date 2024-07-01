from django.db import models
from contabilidad.models import Gasto

class Publicidad(models.Model):
    nombre_campaña = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    valoracion = models.CharField(max_length=20, choices=(
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
        ('Malo', 'Malo'),
    ), blank=True, null=True)

    def __str__(self):
        return self.nombre_campaña