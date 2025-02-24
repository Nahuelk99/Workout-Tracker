from django.db import models
from django.contrib.auth.models import User

# Modelo de Ejercicio
class Ejercicio(models.Model):
    CATEGORIAS = [
        ('Cardio', 'Cardio'),
        ('Fuerza', 'Fuerza'),
        ('Flexibilidad', 'Flexibilidad'),
        ('Otro', 'Otro')
    ]
    
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre

# Modelo de Plan de Entrenamiento
class PlanEntrenamiento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="planes_entrenamiento")
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.usuario.username}"

# Modelo de Sesión de Entrenamiento (Ejercución de un plan)
class SesionEntrenamiento(models.Model):
    plan = models.ForeignKey(PlanEntrenamiento, on_delete=models.CASCADE, related_name="sesiones")
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    series = models.IntegerField()
    repeticiones = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fecha_hora = models.DateTimeField()
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.plan.nombre} - {self.ejercicio.nombre} - {self.fecha_hora}"
