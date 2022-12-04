from django.db import models
from django import forms



# Create your models here.

class FarmLocations(models.Model):
 location_name = models.CharField('Location Name', max_length=50)
 location_description = models.CharField(max_length=200, blank=True)

 def __str__(self):
    return self.location_name




  
class Cow(models.Model):
 
 cow_tag = models.CharField(max_length = 30)
 cow_sex = models.CharField(max_length=6, choices=(('male','MALE'), ('female', "FEMALE")), default='female')
 cow_vaccinations = models.CharField(max_length = 30, blank=True)
 cow_location = models.ForeignKey(FarmLocations, blank=True, null=True, on_delete=models.CASCADE)
 cow_notes = models.CharField(max_length = 200, blank=True) 
 cow_PARENT = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children')

 
 def __str__(self):
     return self.cow_tag
