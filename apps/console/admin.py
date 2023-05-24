# Django Imports
from django.contrib import admin

from .models import Access, AccessUser


class AccessAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


class AccessUserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_active")


admin.site.register(Access, AccessAdmin)
admin.site.register(AccessUser, AccessUserAdmin)
