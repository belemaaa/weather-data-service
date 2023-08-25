import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings



class WeatherData(APIView):
    def post(self, request):
        city = request.data['city']
        if city is None:
            return Response({'message': 'city field is required.'})
        
        api_key = settings.OPENWEATHERMAP_API_KEY
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
        data = response.json()

        if response.status_code == 200:
            return Response({
                'weather data': {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description']
                }
            })
        else:
            return Response({'error': 'Could not retrieve weather data'}, status=500)
