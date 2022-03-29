from api.router import router
from addresses.viewsets.address_viewset import AddressViewSet

router.register(r'addresses', AddressViewSet)
