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
from .forms.userforms import BaseUserCreationForm, CustomLoginForm

from faq.models import Faq
from performances.models import Act, Workshop
# credit: https://pypi.org/project/Django-Verify-Email/
from verify_email.email_handler import send_verification_email

USER_SIGNUP_GOAL = 'signup'
USER_LOGIN_GOAL = 'login'
USER_LOGOUT_GOAL = 'logout'

class TicketStatusView(CreateView):
    form_class = BaseUserCreationForm
    form_class_login = AuthenticationForm
    template_name = 'ticketstatus.html'

    def get(self, request, *args, **kwargs):
        context = {
            'faq_list': Faq.objects.order_by('topic')
        }
        if request.user.is_authenticated:
            return render(request, self.template_name, context)
        else:
            return redirect('home')

    def post(self, request, *args, **kwargs):
        if request.POST['form_goal'] == USER_LOGOUT_GOAL:
            logout(request)

            return redirect('home')

class SignUpView(CreateView):
    signup_form = BaseUserCreationForm
    # form_class_signup = BaseUserCreationForm
    login_form = CustomLoginForm
    # success_url = reverse_lazy('login')
    template_name = 'index.html'
    # success_template_name = 'registration/login.html'

    def get(self, request, *args, **kwars):
        context = {
            'login_form': self.login_form,
            'signup_form': self.signup_form,
            'faq_list': Faq.objects.order_by('topic'),
            'act_list': Act.objects.order_by('stage_name'),
            'workshop_list': Workshop.objects.order_by('name'),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {
            'login_form': self.login_form,
            'signup_form': self.signup_form,
            'faq_list': Faq.objects.all(),
            'act_list': Act.objects.order_by('stage_name'),
            'workshop_list': Workshop.objects.order_by('name'),
        }

        # Handle user logout
        if request.POST['form_goal'] == USER_LOGOUT_GOAL:
            if request.user.is_authenticated:
                context['logout'] = True
                logout(request)
            return render(request, self.template_name, context)

        # Handle user signup
        if request.POST['form_goal'] == USER_SIGNUP_GOAL:
            signup_form = self.signup_form(request.POST)
            context['signup_form'] = signup_form
            if signup_form.is_valid():
                inactive_user = send_verification_email(request, signup_form)
                context['signup'] = True
                return render(request, self.template_name, context)
            else:
                context['expand_canvas_right'] = USER_SIGNUP_GOAL
                return render(request, self.template_name, context)
        
        # Handle user login
        if request.POST['form_goal'] == USER_LOGIN_GOAL:
            login_form = self.login_form(data=request.POST)
            context['login_form'] = login_form
            if login_form.is_valid():
                user = authenticate(
                    request,
                    username=login_form.cleaned_data['username'],
                    password=login_form.cleaned_data['password'],
                    )
                if user is not None:
                    login(request, user)
                #return render(request, self.template_name, context)
                return redirect('ticketstatus')
            else:
                # print('login not valid')
                context['expand_canvas_right'] = USER_LOGIN_GOAL

                return render(request, self.template_name, context)

       # Handle any other request

        return render(request, self.template_name, context)

