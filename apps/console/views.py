# Django Imports
from django.contrib.messages.views import SuccessMessageMixin
from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import AccessForm, PolicyForm
from .models import Access, AccessUser, Policy


class AccessListView(ListView):
    model = Access
    context_object_name = "accesses"


class AccessCreateView(SuccessMessageMixin, CreateView):
    model = Access
    form_class = AccessForm
    success_url = reverse_lazy("console:access_list")
    success_message = "Access was created successfully!"


class AccessDeleteView(SuccessMessageMixin, DeleteView):
    model = Access
    success_url = reverse_lazy("console:access_list")
    success_message = "Access was deleted successfully!"

    def get(self, request, *args, **kwargs):
        raise Http404("Only POST method available")


class AccessUpdateView(SuccessMessageMixin, UpdateView):
    model = Access
    form_class = AccessForm
    success_url = reverse_lazy("console:access_list")
    success_message = "Access was updated successfully!"


class PolicyListView(ListView):
    model = Policy
    context_object_name = "policies"


class PolicyCreateView(SuccessMessageMixin, CreateView):
    model = Policy
    form_class = PolicyForm
    success_url = reverse_lazy("console:policy_list")
    success_message = "Policy was created successfully!"


class UserListView(ListView):
    model = AccessUser
    context_object_name = "users"
