# Django Imports
from django.views.generic import ListView

from .models import Access, AccessUser


class AccessListView(ListView):
    model = Access
    context_object_name = "accesses"


class UserListView(ListView):
    model = AccessUser
    context_object_name = "users"
