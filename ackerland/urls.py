# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/

"""ackerland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from accounts.views import SignUpView, TicketStatusView
from performances.views import ProgrammView

urlpatterns = [
    path('', SignUpView.as_view(), name='home'),
    path('ticketstatus/',TicketStatusView.as_view(), name='ticketstatus'),
    path('admin/', admin.site.urls),
    path('programm/', ProgrammView.as_view(), name='programm'),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('accounts/', include('django.contrib.auth.urls')),
    path('verification/', include('verify_email.urls')),
]
