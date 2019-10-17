"""
   Serializer object
"""
from rest_framework import serializers


class WeathersSerializer(serializers.Serializer):
    """
        Weather Serializer
    """
    latitude = serializers.IntegerField(),
    longitude = serializers.IntegerField(),
    service = serializers.CharField(max_length=200),
    temperature = serializers.IntegerField()
