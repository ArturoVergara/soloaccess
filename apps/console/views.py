# Django Imports
from django.views.generic import ListView, TemplateView

from .models import AccessUser


class TestView(TemplateView):
    template_name = "console/example.html"


class UserListView(ListView):
    model = AccessUser
    context_object_name = "users"
