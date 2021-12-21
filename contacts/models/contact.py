from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=300)
    second_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_fields():
        return ['first_name', 'second_name', 'phone', 'created_at']

