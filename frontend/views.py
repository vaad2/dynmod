from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, TemplateView
from frontend import models

class ViewIndex(TemplateView):
    template_name = 'frontend/view_index.html'

    def get_context_data(self, **kwargs):

        usr = models.users
        return super(ViewIndex, self).get_context_data(**kwargs)
    # def get_queryset(self):

