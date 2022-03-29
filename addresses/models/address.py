from django.db import models


class Address(models.Model):
    objects = models.Manager()

    street = models.CharField(max_length=300)

    city = models.CharField(max_length=300)

    country = models.CharField(max_length=30)

    house = models.CharField(max_length=10, null=True, blank=True)

    flat = models.IntegerField(null=True, blank=True)

    zip_code = models.IntegerField(null=True, blank=True)

    @classmethod
    def get_address_title(cls):
        return f'{cls.country} {cls.city} {cls.street} {cls.zip_code}'

    def __str__(self):
        return f'{self.house} {self.street} {self.city}'

    class Meta:
        verbose_name_plural = 'Address'
