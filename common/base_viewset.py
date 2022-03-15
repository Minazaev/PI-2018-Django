from rest_framework.viewsets import ViewSet, ModelViewSet


class BaseViewSet(ViewSet, ModelViewSet):
    queryset = None
    serializer_class = None
