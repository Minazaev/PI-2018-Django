from users.models import CustomUser
from common.base_serializer import BaseSerializer


class StatusSerializer(BaseSerializer):

    class Meta:
        model = CustomUser
        fields = ['status']
