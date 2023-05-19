# Django Imports
from django.urls import path

from .views import AccessDetailView, AccessPanelView

app_name = "panel"
urlpatterns = [
    path("access/", AccessDetailView.as_view(), name="access_detail"),
    path("", AccessPanelView.as_view(), name="home"),
]
