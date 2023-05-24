# Django Imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class AccessUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=320, unique=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "User"

    def get_absolute_url(self):
        return f"/users/{self.pk}/"
