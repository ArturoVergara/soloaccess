# Django Imports
from django.views.generic import TemplateView


class AccessPanelView(TemplateView):
    template_name = "panel/index.html"


class AccessDetailView(TemplateView):
    template_name = "panel/app.html"
