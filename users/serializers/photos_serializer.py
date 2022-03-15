from users.models import Photos
from common.base_serializer import BaseSerializer


class PhotosSerializer(BaseSerializer):
    class Meta:
        model = Photos
        fields = '__all__'
