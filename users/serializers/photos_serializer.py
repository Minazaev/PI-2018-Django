from rest_framework import serializers
from users.models import Photos


class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'
