from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import CustomUser
from users.serializers.status_serializer import StatusSerializer, StatusSerializerPopulated
from users.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    default_serializer_class = UserSerializer

    @action(detail=True, methods=['GET'], serializer_class=StatusSerializer)
    def status(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        serializer = self.get_serializer(user, context={'request': request})

        return Response(serializer.data)

    @action(detail=True, methods=['PUT'], url_path='set_status', serializer_class=StatusSerializerPopulated)
    def set_status(self, request, pk):
        user = CustomUser.objects.filter(pk=pk)
        serializer = self.get_serializer(data=request.data, context={'request': request}, partial=True)

        if serializer.is_valid():
            user.update(status=request.data.get('status.status'))
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        serializer = UserSerializer(self.queryset, many=True, context={'request': request})
        return Response(data=serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     user = self.get_object()
    #     serializer = StatusSerializer()
    #     # status = request.data['status']
    #     # instance = self.get_object()
    #
    #     return Response(serializer.data)

