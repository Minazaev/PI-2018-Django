from common.base_serializer import BaseSerializer
from profiles.models.profiles import Profile


class ProfileSerializer(BaseSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
