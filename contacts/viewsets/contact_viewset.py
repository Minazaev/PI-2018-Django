from api.serializers import DualSerializerViewSet
from contacts.models.contact import Contact
from rest_framework.response import Response
from contacts.serializers.contact_serializer import ContactSerializer, ContactSerializerPopulated, ContactSerializerPopulatedPopulated
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action


class ContactViewSet(DualSerializerViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializerPopulatedPopulated

    default_serializer_class = ContactSerializerPopulatedPopulated

    serializer_classes = {
        'create': ContactSerializerPopulatedPopulated,
        'update': ContactSerializerPopulatedPopulated
    }

    def list(self, request, **kwargs):
        serializer_context = {'request': request}
        serializer = ContactSerializer(self.queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        serializer_context = {'request': request}
        contact = get_object_or_404(self.queryset, pk=pk)
        serializer = ContactSerializer(contact, many=False, context=serializer_context)
        return Response(serializer.data)



    @action(methods=['post'], detail=True, permission_classes=[IsAdminUser])
    def post(self, request):
        return Response()

