from django.urls import path, include
from .views import UserViewSet, LocationViewSet, PhotoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'photos', PhotoViewSet, basename='photo')
urlpatterns = router.urls


