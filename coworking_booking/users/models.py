from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone Number")

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username