from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ejercicio, PlanEntrenamiento, SesionEntrenamiento
from django.utils import timezone

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class SesionEntrenamientoSerializer(serializers.ModelSerializer):
    ejercicio = EjercicioSerializer(read_only=True)  # Para mostrar detalles del ejercicio
    ejercicio_id = serializers.PrimaryKeyRelatedField(
        source='ejercicio', 
        queryset=Ejercicio.objects.all(),
        write_only=True
    )
    plan_id = serializers.PrimaryKeyRelatedField(
        source='plan', 
        queryset=PlanEntrenamiento.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = SesionEntrenamiento
        fields = ['id', 'series', 'repeticiones', 'peso', 'fecha_hora', 
                 'comentarios', 'ejercicio', 'plan', 'ejercicio_id', 'plan_id']
        extra_kwargs = {
            'plan': {'write_only': True, 'required': False},
            'fecha_hora': {'default': timezone.now}
        }
    
    def create(self, validated_data):
        return SesionEntrenamiento.objects.create(**validated_data)

class PlanEntrenamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEntrenamiento
        fields = ['id', 'nombre', 'fecha_creacion', 'usuario']
        read_only_fields = ['usuario', 'fecha_creacion'] 

class UserSerializer(serializers.ModelSerializer):
    planes_entrenamiento = PlanEntrenamientoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'planes_entrenamiento']
