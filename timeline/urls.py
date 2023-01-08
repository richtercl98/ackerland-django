# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/

from django.urls import path
from .views import Timeline

urlpatterns = [
    path('', Timeline.as_view(), name='timeline'),
]
