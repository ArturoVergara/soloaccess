# Django Imports
from django.contrib import admin

from .models import Access, AccessUser, Policy


class AccessAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "is_disable")


class PolicyAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "is_disable")


class AccessUserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_active")


admin.site.register(Access, AccessAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(AccessUser, AccessUserAdmin)
