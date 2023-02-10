from django.db import models

# Create your models here.

class Fleet(models.Model):
    plate_number = models.CharField(blank=False, max_length=200)
    mileage = models.IntegerField(blank=False)
    manufacturer = models.CharField(max_length=200, blank=False)
    date_of_purchase = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return f'MANUFACTURER: {self.manufacturer} PLATE NUMBER: {self.plate_number} DATE PURCHASED: {self.date_of_purchase}'
    
class Driver(models.Model):
    name = models.CharField(max_length=22)
    phone_number = models.IntegerField()
    age = models.IntegerField()
    cars = models.ManyToManyField(Fleet, related_name="drivers")
    date_hired = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return "NAME: "+ self.name + " AGE: " + str(self.age) + " DATE HIRED: " + str(self.date_hired)
    
