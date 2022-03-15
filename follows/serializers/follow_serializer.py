from follows.models.follow import Follow
from common.base_serializer import BaseSerializer


class FollowSerializer(BaseSerializer):

    class Meta:
        model = Follow
        fields = '__all__'
