"""
    Test app
"""
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .objects.Weather import Weather
from .serializers import WeathersSerializer



class BaseViewTest(APITestCase):
    """
        Class to test view api
    """
    client = APIClient()
    @staticmethod
    def create_weather(latitude=0, longitude=0, service="", temperature=0):
        """
            Create class to add weathers
        """
        weather = Weather(latitude, longitude, service, temperature)
        return weather

    def setUp(self):
        """
            Create weather object tests
        """
        weather_list = []
        weather_list.append(self.create_weather(50, 122, "noaa", 15))
        weather_list.append(self.create_weather(30, 22, "weather.com", 10))
        weather_list.append(self.create_weather(10, 10, "weather.com", 20))
        weather_list.append(self.create_weather(44, 55, "accuweather", 30))
        return weather_list


class GetAllWeatherTest(BaseViewTest):
    """
        Get All Weather Test class
    """
    def test_get_weather(self):
        """
            Return all weathers by service, longitude, latitude and temperature
        """
        response = self.client.get(
            reverse("weathers-all")
        )
        # expected = self.setUp()
        # serialized = WeathersSerializer(expected, many=True)
        # self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
