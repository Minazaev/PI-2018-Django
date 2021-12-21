from rest_framework.routers import DefaultRouter

router = DefaultRouter()


def register_route(prefix, viewset, base_name):
    router.register(prefix, viewset, base_name)
