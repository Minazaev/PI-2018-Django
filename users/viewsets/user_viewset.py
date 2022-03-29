from rest_framework.response import Response
from users.models import CustomUser
from common.base_viewset import BaseViewSet
from users.serializers.user_serializer import UserSerializer


class UserViewSet(BaseViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        serializer = UserSerializer(self.queryset, many=True, context={'request': request})
        return Response(data=serializer.data)
