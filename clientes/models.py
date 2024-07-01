from django.db import models
from programas.models import Programa  # Importa el modelo Programa
from django.utils import timezone

class Cliente(models.Model):
    PAGO_FRACCIONADO_UNIDADES = (
        ('D', 'Días'),
        ('S', 'Semanas'),
        ('M', 'Meses'),
        ('A', 'Años')
    )

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    numero_cliente = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=False)
    programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_pago = models.DateField(default=timezone.now)
    pago_fraccionado = models.BooleanField(default=False)
    duracion_fraccionada = models.PositiveIntegerField(blank=True, null=True)
    unidad_duracion_fraccionada = models.CharField(max_length=1, choices=PAGO_FRACCIONADO_UNIDADES, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.programa:
            self.activo = True
            if self.pago_fraccionado:
                # Asegurar que el precio del programa se divide correctamente
                self.precio_total = self.programa.precio
        else:
            self.activo = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'