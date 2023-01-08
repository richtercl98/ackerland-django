# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/

from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
