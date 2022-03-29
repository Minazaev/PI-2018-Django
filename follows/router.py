from api.router import router
from follows.viewsets.followers_viewset import FollowViewSet

router.register(r'follows', FollowViewSet)
