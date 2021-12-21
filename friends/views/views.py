from friends.models.friend import Friend
from rest_framework import viewsets
from rest_framework.response import Response
from friends.serializer.friend_serializer import FriendSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action


class FriendViewSet(viewsets.ViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def list(self, request):
        serializer_context = {'request': request}
        serializer = FriendSerializer(self.queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def get(self, request):
        return Response()

    @action(methods=['post'], detail=True, permission_classes=[IsAdminUser])
    def post(self, request):
        return Response()

