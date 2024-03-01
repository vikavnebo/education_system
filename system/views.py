from django.views.generic import TemplateView

from system.models import *


class IndexPage(TemplateView):
    template_name = "system/index.html"
