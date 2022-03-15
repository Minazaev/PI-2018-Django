from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action

from users.models import CustomUser
from common.base_viewset import BaseViewSet
from users.serializers.user_serializer import UserSerializer
from users.serializers.status_serializer import StatusSerializer


class UserViewSet(BaseViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['GET', 'PUT'], serializer_class=StatusSerializer)
    def status(self, request, pk):
        if request.method == 'GET':
            user = CustomUser.objects.get(pk=pk)
            serializer = self.get_serializer(user, context={'request': request})
            return Response(serializer.data)

        if request.method == 'PUT':
            user = CustomUser.objects.filter(pk=pk)
            serializer = self.get_serializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                user.update(status=request.data.get('status'))
                return JsonResponse(serializer.data)
            elif not serializer.is_valid():
                return Response(serializer.errors)

    def list(self, request, *args, **kwargs):
        serializer = UserSerializer(self.queryset, many=True, context={'request': request})
        return Response(data=serializer.data)
