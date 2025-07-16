from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['id', 'url', 'shortCode', 'createdAt', 'updatedAt', 'accessCount']
        read_only_fields = ['id', 'shortCode', 'createdAt', 'updatedAt', 'accessCount']
