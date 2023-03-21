# credit: https://www.olivierpons.com/2022/01/27/django-scripting-appregistrynotready-apps-arent-loaded-yet-solution/
import django
django.setup()

from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


# from phonenumber_field.formfields import RegionalPhoneNumberField

from ..models import User

from django.core.exceptions import ValidationError

# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
# TODO: better name
class BaseUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(BaseUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        users_with_same_email = User.objects.filter(email=email)
        if users_with_same_email.count():
            raise ValidationError('E-Mail "%(email)s" wird bereits verwendet.', code='email-taken', params={'email' : email})
        return email

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'password1', 'password2', 'vorname', 'nachname', 'email', 'eingeladen_von']
        help_texts = {
            'username': 'Diesen Benutzernamen musst du dir merken, damit du dich später wieder einloggen kannst, um deine Ticketinformationen abzurufen',
            'password1': None,
            'password2': None,
        }


# TODO: better name
class BaseUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ['vorname', 'nachname']

class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'