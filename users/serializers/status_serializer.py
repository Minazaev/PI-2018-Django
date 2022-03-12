from users.models import CustomUser
from rest_framework import serializers

from users.serializers.user_serializer import UserSerializer


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['status']


class StatusSerializerPopulated(serializers.ModelSerializer):
    status = StatusSerializer()
    # status = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['status']
