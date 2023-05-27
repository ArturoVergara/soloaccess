# Standard Libraries
import uuid

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


class Access(models.Model):
    class Types(models.IntegerChoices):
        HTTP = 0, "HTTP"
        SSH = 1, "SSH"

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    type = models.PositiveSmallIntegerField(choices=Types.choices)
    image = models.ImageField(blank=True, null=True)
    observation = models.TextField(blank=True, null=True)
    is_disable = models.BooleanField(default=False)

    allowed_users = models.ManyToManyField(
        "AccessUser",
        blank=True,
        related_name="accesses_allowed_user",
        help_text="Select explicit allowed users for this access",
    )
    denied_users = models.ManyToManyField(
        "AccessUser",
        blank=True,
        related_name="accesses_denied_user",
        help_text="Select explicit denied users for this access",
    )

    class Meta:
        verbose_name_plural = "Accesses"

    def __str__(self):
        return f"{self.name} ({self.pk})"


class Policy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_disable = models.BooleanField(default=False)

    accesses = models.ManyToManyField(
        "Access",
        blank=True,
        related_name="policies_access",
        help_text="Select accesses for this policy",
    )
    users = models.ManyToManyField(
        "AccessUser",
        blank=True,
        related_name="policies_user",
        help_text="Select users for this policy",
    )
