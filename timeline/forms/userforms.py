# credit: https://www.olivierpons.com/2022/01/27/django-scripting-appregistrynotready-apps-arent-loaded-yet-solution/
import django
django.setup()

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ..models import User

# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
# TODO: better name
class BaseUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ['vorname', 'nachname', 'bezahlt']


# TODO: better name
class BaseUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ['vorname', 'nachname', 'bezahlt']
