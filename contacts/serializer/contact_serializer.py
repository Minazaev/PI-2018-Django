from contacts.models.contact import Contact
from serializer.custom_base_serializer import CustomBaseSerializer


class ContactSerializer(CustomBaseSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
