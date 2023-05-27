# Django Imports
from django import forms

from .models import Access, Policy


class AccessForm(forms.ModelForm):
    class Meta:
        model = Access
        fields = ("name", "type", "observation", "image", "is_disable")


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ("name", "description", "is_disable")
