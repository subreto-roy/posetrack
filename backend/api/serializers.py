# api/serializers.py
from rest_framework import serializers
from .models import PostureData

class PostureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostureData
        fields = '__all__'