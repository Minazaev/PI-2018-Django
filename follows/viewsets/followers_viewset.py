from api.serializers import DualSerializerViewSet
from follows.models.follow import Follow
from follows.serializers.follow_serializer import FollowSerializer


class FollowViewSet(DualSerializerViewSet):
    queryset = Follow.objects.all()

    serializer_classes = {
        'create': FollowSerializer,
        'update': FollowSerializer
    }

    default_serializer_class = FollowSerializer
