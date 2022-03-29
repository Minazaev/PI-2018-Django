from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from django.contrib import admin


@admin.register(CustomUser)
class UsersAdmin(UserAdmin):
    pass


