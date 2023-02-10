from django.shortcuts import render
from .models import Car, Driver
from .serializers import CarSerializer, DriverSerializer
from rest_framework import generics

# Create your views here.

# fleet
class FleetListView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    

class FleetUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    
class FleetDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    
# drivers
class DriverListView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    
class DriverUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    
    
    
    
