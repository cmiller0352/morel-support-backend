from django.shortcuts import render
from .models import (User, Photo, Location)
from .serializers import (PhotoSerializer, UserSerializer, LocationSerializer)
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class LocationViewSet(viewsets.ModelViewSet):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

class PhotoViewSet(viewsets.ModelViewSet):
  queryset = Photo.objects.all()
  serializer_class = PhotoSerializer


