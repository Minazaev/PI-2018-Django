from profiles.models.profiles import Profile
from common.base_viewset import BaseViewSet
from profiles.serializers.profile_serializer import ProfileSerializer


class ProfileViewSet(BaseViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
