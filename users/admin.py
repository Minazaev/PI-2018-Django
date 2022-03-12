from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser, Photos
from django.contrib import admin


@admin.register(CustomUser)
class UsersAdmin(UserAdmin):
    pass


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    pass

