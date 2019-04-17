from rest_framework import serializers
from .models import Photo, User, Location

class PhotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Photo
    fields = ['user', 'photo_url']

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email']

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = ['photo', 'latitude', 'longitude']



