from django.db import models
from addresses.models.address import Address
from users.models import CustomUser


class Contact(models.Model):
    objects = models.Manager()

    first_name = models.CharField(max_length=300)
    second_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.user}'
