from api.serializers import UserSerializer
from contacts.models.contact import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class ContactSerializerPopulated(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Contact
        fields = '__all__'
