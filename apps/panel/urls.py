# Django Imports
from django.urls import path

from .views import AppsPanelView

app_name = "panel"
urlpatterns = [
    path("", AppsPanelView.as_view(), name="home"),
]
