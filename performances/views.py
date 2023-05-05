from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from performances.models import Act, Workshop
# Create your views here.

class LineupView(TemplateView):
    template_name = 'verification_mail.html' # TODO neues HTML File

    def get(self, request, *args, **kwargs):
        context = {
            'act_list': Act.objects.order_by('name')
        }

        if request.user.is_authenticated:
            return render(request, self.template_name, context)
        else:
            return redirect('home')

class WorkshopView(TemplateView):
    template_name = 'verification_mail.html' # TODO neues HTML File

    def get(self, request, *args, **kwargs):
        context = {
            'workshop_list': Workshop.objects.order_by('name')
        }

        if request.user.is_authenticated:
            return render(request, self.template_name, context)
        else:
            return redirect('home')
