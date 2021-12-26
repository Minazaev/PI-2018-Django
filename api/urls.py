from django.contrib import admin
from django.urls import path, include

from api.views import UserViewSet
from contacts.viewsets.contact_view_set import ContactViewSet
from friends.viewsets.friend_view_set import FriendViewSet
from api.router import register_route, router


register_route(r'users', UserViewSet)
register_route(r'contacts', ContactViewSet)
register_route(r'friends', FriendViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

