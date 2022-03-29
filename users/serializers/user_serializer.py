from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from follows.models.follow import Follow
from users.models import CustomUser
from common.base_serializer import BaseSerializer


class UserSerializer(BaseSerializer):
    name = serializers.CharField(source='first_name')

    followed = serializers.SerializerMethodField()

    permission_classes = [IsAuthenticated]

    def get_followed(self, user):
        me = self.context['request'].user

        if me.is_anonymous:
            return False

        return Follow.objects.filter(follower=me, followed=user).exists()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'first_name', 'last_name', 'followed']
