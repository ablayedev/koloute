from rest_framework import serializers
from register.models import Location,Station


class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields="__all__"

class StationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Station
        fields="__all__"
        