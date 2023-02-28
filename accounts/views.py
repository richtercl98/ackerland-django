from django.shortcuts import render, redirect
# Create your views here.

# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
# accounts/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms.userforms import BaseUserCreationForm
# credit: https://pypi.org/project/Django-Verify-Email/
from verify_email.email_handler import send_verification_email

USER_SIGNUP_GOAL = 'signup'
USER_LOGIN_GOAL = 'login'
USER_LOGOUT_GOAL = 'logout'

class TicketStatusView(CreateView):
    form_class = BaseUserCreationForm
    form_class_login = AuthenticationForm
    template_name = 'app/ticketstatus.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user.is_authenticated)
            return render(request, self.template_name)
        else:
            return redirect('home')

    def post(self, request, *args, **kwargs):
        if request.POST['form_goal'] == USER_LOGOUT_GOAL:
            logout(request)
            return HttpResponse('Logout successful. <a href="/">Return to Homepage</a>')

class SignUpView(CreateView):
    form_class = BaseUserCreationForm
    # form_class_signup = BaseUserCreationForm
    form_class_login = AuthenticationForm
    # success_url = reverse_lazy('login')
    template_name = 'signup.html'
    # success_template_name = 'registration/login.html'

    def get(self, request, *args, **kwars):
        return render(request, self.template_name, {
            'login_form': self.form_class_login,
            'register_form': self.form_class,
            })

    def post(self, request, *args, **kwargs):
        if request.POST['form_goal'] == USER_LOGOUT_GOAL:
            logout(request)
            return HttpResponse('Logout successful. <a href="/">Return to Homepage</a>')
        if request.POST['form_goal'] == USER_SIGNUP_GOAL:
            form = self.form_class(request.POST)
            if form.is_valid():
                inactive_user = send_verification_email(request, form)
                return HttpResponse('Verification Link has been sent to email provided. Follow instructions given in email. <a href="/">Return to Homepage</a>')
            else:
                print('login not valid')
                return render(request, self.template_name, {
                    'login_form': form,
                    'register_form' : form,
                    'expand_canvas_right': True,
                    })
        if request.POST['form_goal'] == USER_LOGIN_GOAL:
            form = self.form_class_login(data=request.POST)
            if form.is_valid():
                user = authenticate(
                    request,
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    )
                if user is not None:
                    login(request, user)
                return HttpResponse('Login successful. <a href="/">Return to Homepage</a>')
            else:
                print('login not valid')
                return render(request, self.template_name, {
                    'login_form': form,
                    'register_form' : form,
                    'expand_canvas_right': True,
                    })

        return render(request, self.template_name, {
            'login_form': form,
            'register_form': form,
            })

