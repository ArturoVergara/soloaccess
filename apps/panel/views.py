# Django Imports
from django.views.generic import TemplateView


class AppsPanelView(TemplateView):
    template_name = "panel/example.html"
