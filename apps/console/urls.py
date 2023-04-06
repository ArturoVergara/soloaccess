# Django Imports
from django.urls import path

from .views import TestView

app_name = "console"
urlpatterns = [
    path("", TestView.as_view(), name="test_view"),
]
