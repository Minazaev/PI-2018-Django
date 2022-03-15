from common.base_viewset import BaseViewSet
from follows.models.follow import Follow
from follows.serializers.follow_serializer import FollowSerializer


class FollowViewSet(BaseViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
