from api.router import router
from users.viewsets.user_viewset import UserViewSet

router.register(r'users', UserViewSet)
