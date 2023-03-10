from django.shortcuts import render

# Create your views here.

from .models import Floor, Timeslot, DiscJockey
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.forms.models import model_to_dict

class Timeline(TemplateView):
    template_name = 'timeline.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lineup'] = []

        floor_info = {}
        for floor in Floor.objects.all():
            timeslots = Timeslot.objects.filter(location=floor)
            lineup = []
            for timeslot in timeslots:
                 timeslot_dic = model_to_dict(timeslot)
                 timeslot_dic['acts'] = [model_to_dict(act) for act in timeslot.acts.all()]
                 lineup.append(timeslot_dic)
            context['lineup'].append({
                'name' : floor.name,
                'timetable' : lineup,
                })

        # print(context)
        return context
