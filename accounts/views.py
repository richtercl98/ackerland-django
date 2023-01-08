from django.shortcuts import render

# Create your views here.

# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
# accounts/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms.userforms import BaseUserCreationForm


class SignUpView(CreateView):
    form_class = BaseUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
