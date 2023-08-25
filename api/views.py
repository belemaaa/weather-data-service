from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings
from .serializers import WeatherSerializer


class WeatherData(APIView):
    def post(self, request):
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            city = serializer.validated_data.get('city')
            if city is None:
                return Response({'message': 'city field is required.'})
            
            api_key = settings.OPENWEATHERMAP_API_KEY
            
