# Django Imports
from django.urls import path

from .views import TestView, UserListView

app_name = "console"
urlpatterns = [
    path("users", UserListView.as_view(), name="user_list"),
    path("", TestView.as_view(), name="test_view"),
]
