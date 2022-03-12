from rest_framework import serializers
from follows.models.follow import Follow
from users.models import CustomUser
from users.serializers.photos_serializer import PhotosSerializer


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    photos = PhotosSerializer()

    followed = serializers.SerializerMethodField()

    def get_followed(self, user):
        me = self.context['request'].user

        if me.is_anonymous:
            return False

        return Follow.objects.filter(follower=me, followed=user).exists()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'status', 'photos', 'first_name', 'last_name', 'followed']
