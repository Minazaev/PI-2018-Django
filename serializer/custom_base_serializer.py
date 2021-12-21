from rest_framework import serializers


class CustomBaseSerializer(serializers.ModelSerializer):
    url = None

    @staticmethod
    def get_serializer(view_name=None, read_only=None):
        return serializers.ModelSerializer()

