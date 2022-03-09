from django.contrib import admin
from django.urls import path, include

from contacts.viewsets.contact_viewset import ContactViewSet
from friends.viewsets.friend_viewset import FriendViewSet
from addresses.viewsets.address_viewset import AddressViewSet
from users.viewsets.user_views import UserViewSet
from api.router import register_route, router


register_route(r'users', UserViewSet)
register_route(r'contacts', ContactViewSet)
register_route(r'friends', FriendViewSet)
register_route(r'addresses', AddressViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

