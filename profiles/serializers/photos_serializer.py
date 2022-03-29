from rest_framework.permissions import IsAuthenticated

from profiles.models.profiles import Profile, Photos
from common.base_serializer import BaseSerializer


class PhotosSerializer(BaseSerializer):

    class Meta:
        model = Photos
        # fields = ['photos']
        fields = '__all__'
        # fields = ['small', 'large']
