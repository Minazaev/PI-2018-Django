from api.serializers import DualSerializerViewSet
from contacts.models.contact import Contact
from rest_framework.response import Response
from contacts.serializers.contact_serializer import ContactSerializerPopulated
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action


class ContactViewSet(DualSerializerViewSet):
    queryset = Contact.objects.prefetch_related().all()
    # serializer_class = ContactSerializerPopulated

    default_serializer_class = ContactSerializerPopulated

    serializer_classes = {
        'create': ContactSerializerPopulated,
        'update': ContactSerializerPopulated
    }

    @action(methods=['post'], detail=True, permission_classes=[IsAdminUser])
    def post(self):
        return Response()

