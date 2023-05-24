# Django Imports
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from .views import AccessListView, UserListView

app_name = "console"
urlpatterns = [
    path("accesses", AccessListView.as_view(), name="access_list"),
    path("users", UserListView.as_view(), name="user_list"),
    path(
        "",
        RedirectView.as_view(url=reverse_lazy("console:access_list")),
        name="home",
    ),
]
