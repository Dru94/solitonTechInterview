from rest_framework import serializers
from .models import Car, Driver



# class C(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = '__all__'

# class DriverSerializer(serializers.ModelSerializer):
#     cars = FleetSerializer(many=True)
#     class Meta:
#         model = Driver
#         fields = "__all__"
        
#     def create(self, validated_data):
#         cars_data = validated_data.pop('cars')
#         driver = Driver.objects.create(**validated_data)

#         for car_data in cars_data:
#             Fleet.objects.create(driver=driver, **car_data)
#         return driver


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'plate_number', 'mileage', 'manufacturer', 'drivers']

class DriverSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, )

    class Meta:
        model = Driver
        fields = ['id', 'name', 'phone_number', 'age','cars']
        
    def create(self, validated_data):
        car_data = validated_data.pop('cars')
        driver = Driver.objects.create(**validated_data)
        for car in car_data:
            car, created = Car.objects.get_or_create(**car_data)
            driver.car.add(car)
        return driver
