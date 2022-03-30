from django.contrib import admin

from .models import Profile, Contacts, Photos

admin.site.register(Profile)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    pass