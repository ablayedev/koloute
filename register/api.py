from rest_framework import viewsets,permissions
from .serializers import LocationSerializers,StationSerializers
from .models import Location,Station


class LocationViewset(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    queryset=Location.objects.all()
    serializer_class=LocationSerializers

class StationViewset(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    queryset=Station.objects.all()
    serializer_class=StationSerializers