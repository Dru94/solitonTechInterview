from django.shortcuts import render
from .models import Fleet, Driver
from .serializers import FleetSerializer, DriverSerializer
from rest_framework import generics

# Create your views here.

# fleet
class FleetListView(generics.ListCreateAPIView):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
    

class FleetUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
    
    
class FleetDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
    
    
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
    
    
    
    
