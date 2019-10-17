"""
    Views Rest
"""
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import get_weathers_accuweather, get_weathers_noaa, post_weathers_weatherdotcom

class WeatherList(APIView):
    """
        Weather List View
    """
    def get(self, request):
        """
            Get weather by longitude, latitude and service
        """
        longitude = self.request.query_params.get('longitude')
        latitude = self.request.query_params.get('latitude')
        services = self.request.query_params.get('services')
        list_weather = []
        if longitude is None or latitude is None or services is None:
            return Response({"Status":"Error", "Message":"Latitude, longitude and services mustn't be empty"})
        if -90 <= float(latitude) <= 90 and -180 <= float(longitude) <= 180:
            services_weather = services.split(",")
            for serv in services_weather:
                if serv == "accuweather_Weather":
                    list_weather.append(get_weathers_accuweather(latitude, longitude))
                elif serv == "noaa_Weather":
                    list_weather.append(get_weathers_noaa(','.join([latitude, longitude])))
                elif serv == "weatherdotcom_Weather":
                    list_weather.append(post_weathers_weatherdotcom(latitude, longitude))
            return Response(list_weather)
        else:
            return Response({"Status":"Error", "Message":"The latitude must be a number between -90 and 90 and the longitude between -180 and 180."})
