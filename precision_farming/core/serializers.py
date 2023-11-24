from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    pH = serializers.FloatField()
    water_level = serializers.CharField()
    soil_type = serializers.CharField()
    location = serializers.CharField()