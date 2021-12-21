from rest_framework import serializers
from contacts.models.contact import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(
        view_name='contact-detail',
        read_only=True
    )

    class Meta:
        model = Contact
        fields = '__all__'

