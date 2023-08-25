from django.urls import path
from .import views

urlpatterns = [
    path('weather-data/', views.WeatherData.as_view()),
]

endpoint = 'http://127.0.0.1:8000/api/weather-data/'