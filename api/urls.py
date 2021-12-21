"""api URL Configuration

The `urlpatterns` list routes URLs to view_set. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function view_set
    1. Add an import:  from my_app import view_set
    2. Add a URL to urlpatterns:  path('', view_set.home, name='home')
Class-based view_set
    1. Add an import:  from other_app.view_set import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from contacts.view_set.contact_view_set import ContactViewSet
from friends.view_set.friend_view_set import FriendViewSet
from rest_framework import serializers, viewsets
from router.router import register_route, router


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
    path(r'contact/<int:id>/', ContactViewSet.as_view({'get': 'retrieve'}), name='contact-detail')
]

