import requests
import pytz
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings
from datetime import datetime, timedelta


class WeatherData(APIView):
    def post(self, request):
        city = request.data['city']
        if city is None:
            return Response({'message': 'city field is required.'}, status=status.HTTP_400_BAD_REQUEST)
          
        api_key = settings.OPENWEATHERMAP_API_KEY
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
        data = response.json()

        if response.status_code == 200:
            timezone_offset = data['timezone']
            utc_offset = timedelta(seconds=timezone_offset)
            
            utc_time = datetime.utcnow()
            local_time = utc_time + utc_offset
            return Response({
                'weather data': {
                    'city': data['name'],
                    'timezone': local_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'description': data['weather'][0]['description']
                }
            })
        else:
            return Response({'error': 'Could not retrieve weather data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
