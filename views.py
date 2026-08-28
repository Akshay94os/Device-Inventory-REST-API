from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Device
from .serializers import DeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('-created_at')
    serializer_class = DeviceSerializer

@api_view(['GET'])
def health_metrics(request):
    total = Device.objects.count()
    online = Device.objects.filter(is_online=True).count()
    return Response({
        "status": "operational",
        "total_devices": total,
        "online_count": online,
        "offline_count": total - online
    })
