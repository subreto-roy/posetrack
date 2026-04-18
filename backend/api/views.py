from rest_framework import viewsets
from .models import PostureData
from .serializers import PostureDataSerializer

class PostureDataViewSet(viewsets.ModelViewSet):
    queryset = PostureData.objects.all()
    serializer_class = PostureDataSerializer