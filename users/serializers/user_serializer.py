from rest_framework import serializers
from users.models import CustomUser
from users.serializers.photos_serializer import PhotosSerializer


class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(source='date_joined')
    name = serializers.CharField(source='first_name')
    photos = PhotosSerializer()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'status', 'photos', 'first_name', 'last_name', 'created_at']
