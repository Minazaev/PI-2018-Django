from django.contrib import admin
from addresses.models.address import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
