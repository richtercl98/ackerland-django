from django.shortcuts import render
# Create your views here.

# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
# accounts/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .forms.userforms import BaseUserCreationForm
# credit: https://pypi.org/project/Django-Verify-Email/
from verify_email.email_handler import send_verification_email

class SignUpView(CreateView):
    form_class = BaseUserCreationForm
    # success_url = reverse_lazy('login')
    template_name = 'signup.html'
    # success_template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            return HttpResponse('Verification Link has been sent to email provided. Follow instructions given in email.')

        return render(request, self.template_name, {'form':form})
