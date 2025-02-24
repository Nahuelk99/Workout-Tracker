import os
import django

# Configurar Django en el script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workout_tracker.settings')
django.setup()

from core.models import Ejercicio

# Lista de ejercicios a insertar
ejercicios = [
    {"nombre": "Sentadilla", "descripcion": "Ejercicio para piernas y glúteos", "categoria": "Fuerza"},
    {"nombre": "Flexiones", "descripcion": "Ejercicio para pectorales y tríceps", "categoria": "Fuerza"},
    {"nombre": "Trotar", "descripcion": "Ejercicio aeróbico de resistencia", "categoria": "Cardio"},
    {"nombre": "Plancha", "descripcion": "Ejercicio isométrico para el core", "categoria": "Flexibilidad"}
]

# Insertar datos si no existen
for data in ejercicios:
    Ejercicio.objects.get_or_create(nombre=data["nombre"], defaults=data)

print("✅ Datos insertados correctamente.")
