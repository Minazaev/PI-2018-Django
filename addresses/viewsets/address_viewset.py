from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from addresses.serializers.address_serializer import AddressSerializer
from addresses.models.address import Address
from common.base_viewset import BaseViewSet


class AddressViewSet(BaseViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def list(self, request, **kwargs):
        serializer_context = {'request': request}
        serializer = AddressSerializer(self.queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        serializer_context = {'request': request}
        address = get_object_or_404(self.queryset, pk=pk)
        serializer = AddressSerializer(address, many=False, context=serializer_context)
        return Response(serializer.data)
