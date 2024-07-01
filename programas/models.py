# programas/models.py

from django.db import models

class Programa(models.Model):
    DURACION_UNIDADES = (
        ('D', 'Días'),
        ('S', 'Semanas'),
        ('M', 'Meses'),
        ('A', 'Años')
    )

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    recurrente = models.BooleanField(default=False)
    duracion = models.PositiveIntegerField(blank=True, null=True)
    unidad_duracion = models.CharField(max_length=1, choices=DURACION_UNIDADES, blank=True, null=True)

    def __str__(self):
        return self.nombre