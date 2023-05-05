from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from performances.models import Act, Workshop
# Create your views here.

class ProgrammView(TemplateView):
    template_name = 'programm.html'

    def get(self, request, *args, **kwargs):
        context = {
            'act_list': Act.objects.order_by('stage_name'),
            'workshop_list': Workshop.objects.order_by('name')
        }

        return render(request, self.template_name, context)
