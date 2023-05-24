# Django Imports
from django.contrib import admin

from .models import AccessUser


class AccessUserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_active")


admin.site.register(AccessUser, AccessUserAdmin)
