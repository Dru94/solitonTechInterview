from rest_framework import serializers
from .models import Fleet, Driver



class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    cars = FleetSerializer(many=True)
    class Meta:
        model = Driver
        fields = "__all__"
        
    def create(self, validated_data):
        cars_data = validated_data.pop('cars')
        driver = Driver.objects.create(**validated_data)

        for car_data in cars_data:
            Fleet.objects.create(driver=driver, **car_data)
        return driver
