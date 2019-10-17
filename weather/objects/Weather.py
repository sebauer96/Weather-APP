"""
    Object Weather
"""
class Weather(object):
    """
        Constructor Weather
    """
    latitude = 0
    longitude = 0
    service = ""
    temperature = 0
    def __init__(self, latitude, longitude, service, temperature):
        self.latitude = latitude
        self.longitude = longitude
        self.service = service
        self.temperature = temperature
