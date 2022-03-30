from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser):
    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

    # def __unicode__(self):
    #     return self.get_full_name()
