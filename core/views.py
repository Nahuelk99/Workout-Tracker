from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ejercicio, PlanEntrenamiento, SesionEntrenamiento
from .serializers import EjercicioSerializer, PlanEntrenamientoSerializer, SesionEntrenamientoSerializer, UserSerializer

# Clase de autenticación personalizada para omitir verificación CSRF
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]

class PlanEntrenamientoViewSet(viewsets.ModelViewSet):
    serializer_class = PlanEntrenamientoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [CsrfExemptSessionAuthentication]
    
    def get_queryset(self):
        """Retorna solo los planes del usuario actual"""
        return PlanEntrenamiento.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        """Asigna automáticamente el usuario actual al crear un plan"""
        serializer.save(usuario=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        """Asegura que solo el propietario pueda eliminar el plan"""
        plan = self.get_object()
        if plan.usuario != request.user:
            return Response(
                {"error": "No tienes permiso para eliminar este plan"}, 
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)

class SesionEntrenamientoViewSet(viewsets.ModelViewSet):
    serializer_class = SesionEntrenamientoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [CsrfExemptSessionAuthentication]
    
    def get_queryset(self):
        """Retorna solo las sesiones de los planes del usuario actual"""
        return SesionEntrenamiento.objects.filter(plan__usuario=self.request.user)
    
    def perform_create(self, serializer):
        """Verifica que el plan pertenezca al usuario actual"""
        plan = serializer.validated_data.get('plan')
        if plan.usuario != self.request.user:
            raise permissions.PermissionDenied(
                "No puedes crear sesiones en planes que no te pertenecen"
            )
        serializer.save()

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    authentication_classes = [CsrfExemptSessionAuthentication]
    
    def get_queryset(self):
        """Los usuarios solo pueden ver su propia información"""
        return User.objects.filter(id=self.request.user.id)
    
    def perform_update(self, serializer):
        """Solo permite actualizar ciertos campos"""
        if self.request.user != serializer.instance:
            raise permissions.PermissionDenied(
                "No puedes modificar otros usuarios"
            )
        serializer.save()

def home_view(request):
    """Vista principal que muestra el login con Google"""
    return render(request, 'core/login.html')

@login_required
def dashboard_view(request):
    """Vista del dashboard después del login"""
    return render(request, 'core/dashboard.html', {
        'user': request.user,
        'planes': PlanEntrenamiento.objects.filter(usuario=request.user)
    })