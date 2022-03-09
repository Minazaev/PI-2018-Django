from rest_framework import serializers, viewsets


class DualSerializerViewSet(viewsets.ModelViewSet, viewsets.ViewSet):

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
