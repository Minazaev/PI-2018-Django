from contacts.models.contact import Contact
from rest_framework import viewsets
from rest_framework.response import Response
from contacts.serializer.contact_serializer import ContactSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action


class ContactViewSet(viewsets.ViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request):
        serializer_context = {'request': request}
        serializer = ContactSerializer(self.queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def get(self, request):
        return Response()

    @action(methods=['post'], detail=True, permission_classes=[IsAdminUser])
    def post(self, request):
        return Response()

