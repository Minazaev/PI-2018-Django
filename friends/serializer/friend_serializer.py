from friends.models.friend import Friend
from serializer.custom_base_serializer import CustomBaseSerializer


class FriendSerializer(CustomBaseSerializer):

    class Meta:
        model = Friend
        fields = '__all__'
