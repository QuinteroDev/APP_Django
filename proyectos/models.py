from django.db import models
from contabilidad.models import Ingreso, Gasto

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    ingreso = models.ForeignKey(Ingreso, on_delete=models.SET_NULL, blank=True, null=True, related_name='proyectos')
    gasto = models.ForeignKey(Gasto, on_delete=models.SET_NULL, blank=True, null=True, related_name='proyectos')
    status = models.CharField(max_length=20, choices=(
        ('Por empezar', 'Por empezar'),
        ('En marcha', 'En marcha'),
        ('Finalizado', 'Finalizado'),
    ))

    def __str__(self):
        return self.nombre_proyecto

class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    nombre_tarea = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    status = models.CharField(max_length=20, choices=(
        ('Por empezar', 'Por empezar'),
        ('En marcha', 'En marcha'),
        ('Finalizado', 'Finalizado'),
    ))

    def __str__(self):
        return self.nombre_tarea