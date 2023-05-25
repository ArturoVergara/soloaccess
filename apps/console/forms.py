# Django Imports
from django import forms

from .models import Access


class AccessForm(forms.ModelForm):
    class Meta:
        model = Access
        fields = ("name", "type", "observation", "image", "is_disable")
