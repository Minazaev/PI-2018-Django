from contacts.models.contact import Contact
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from contacts.serializer.contact_serializer import ContactSerializer


class ContactViewSet(viewsets.ViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request):
        queryset = Contact.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = ContactSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

