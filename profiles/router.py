from api.router import router
from profiles.viewsets.profile_viewset import ProfileViewSet

router.register(r'profile', ProfileViewSet)

