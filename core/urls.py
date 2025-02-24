from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    EjercicioViewSet, 
    PlanEntrenamientoViewSet, 
    SesionEntrenamientoViewSet, 
    UserViewSet,
    dashboard_view
)

router = DefaultRouter()
router.register(r'ejercicios', EjercicioViewSet, basename='ejercicio')
router.register(r'planes', PlanEntrenamientoViewSet, basename='plan')
router.register(r'sesiones', SesionEntrenamientoViewSet, basename='sesion')
router.register(r'usuarios', UserViewSet, basename='usuario')

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
]

urlpatterns += router.urls