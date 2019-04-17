from django.db import models
from django.conf import settings

class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=40)
  email = models.EmailField(max_length=50)
  # figure out fb login stuff here
  def __str__(self):
    return self.first_name

class Photo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
  photo_url = models.CharField(max_length=250)
  def __str__(self):
    return self.photo_url

class Location(models.Model):
  photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='locations')
  latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
  longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
  def __str__(self):
        return self.latitude


