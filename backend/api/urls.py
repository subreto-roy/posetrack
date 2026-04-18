from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostureDataViewSet

router = DefaultRouter()
router.register(r'posture', PostureDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]