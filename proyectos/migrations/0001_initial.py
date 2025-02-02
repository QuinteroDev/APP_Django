# Generated by Django 5.0.6 on 2024-07-01 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
                ('status', models.CharField(choices=[('Por empezar', 'Por empezar'), ('En marcha', 'En marcha'), ('Finalizado', 'Finalizado')], max_length=20)),
                ('gasto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos', to='contabilidad.gasto')),
                ('ingreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos', to='contabilidad.ingreso')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tarea', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
                ('status', models.CharField(choices=[('Por empezar', 'Por empezar'), ('En marcha', 'En marcha'), ('Finalizado', 'Finalizado')], max_length=20)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='proyectos.proyecto')),
            ],
        ),
    ]
