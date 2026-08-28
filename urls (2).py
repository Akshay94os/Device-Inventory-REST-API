from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, health_metrics

router = DefaultRouter()
router.register(r'devices', DeviceViewSet, basename='device')

urlpatterns = [
    path('metrics/', health_metrics, name='api_metrics'),
    path('', include(router.urls)),
]
