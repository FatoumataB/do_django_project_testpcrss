from django.shortcuts import render
from .service import get_capsules
from django.views.generic import TemplateView


# Create your views here.
from django.views.generic import TemplateView

class GetCapsules(TemplateView):
    template_name = 'capsules.html'
    def get_context_data(self, *args, **kwargs):
        context= {
            'capsules' : get_capsules(),
            }
        return context