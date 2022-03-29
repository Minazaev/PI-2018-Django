from django.contrib import admin
from profiles.models.profiles import Profile, Contacts, Photos


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    pass
