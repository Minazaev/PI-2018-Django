from django.contrib import admin
from follows.models.follow import Follow


@admin.register(Follow)
class FollowsAdmin(admin.ModelAdmin):
    pass

