from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from contacts.view_set.contact_view_set import ContactViewSet
from friends.view_set.friend_view_set import FriendViewSet
from rest_framework import serializers, viewsets
from api.router import register_route, router


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'is_superuser']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


register_route(r'users', UserViewSet)
register_route(r'contacts', ContactViewSet)
register_route(r'friends', FriendViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

