# Django Imports
from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = "panel/example.html"
