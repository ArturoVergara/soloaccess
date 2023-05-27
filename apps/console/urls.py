# Django Imports
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from .views import (
    AccessCreateView,
    AccessDeleteView,
    AccessListView,
    AccessUpdateView,
    PolicyListView,
    UserListView,
)

app_name = "console"
urlpatterns = [
    path("accesses/<int:pk>/delete/", AccessDeleteView.as_view(), name="access_delete"),
    path("accesses/<int:pk>/edit/", AccessUpdateView.as_view(), name="access_update"),
    path("accesses/add/", AccessCreateView.as_view(), name="access_create"),
    path("accesses/", AccessListView.as_view(), name="access_list"),
    path("policies/", PolicyListView.as_view(), name="policy_list"),
    path("users/", UserListView.as_view(), name="user_list"),
    path(
        "",
        RedirectView.as_view(url=reverse_lazy("console:access_list")),
        name="home",
    ),
]
