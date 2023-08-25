from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.Serializer):
    model = Weather
    fields = ['city']