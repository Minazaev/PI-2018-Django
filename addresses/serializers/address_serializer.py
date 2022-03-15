from addresses.models.address import Address
from common.base_serializer import BaseSerializer


class AddressSerializer(BaseSerializer):

    class Meta:
        model = Address
        fields = '__all__'

