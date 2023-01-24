# credit: https://www.olivierpons.com/2022/01/27/django-scripting-appregistrynotready-apps-arent-loaded-yet-solution/
import django
django.setup()

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from phonenumber_field.formfields import RegionalPhoneNumberField
from ..models import User

# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
# TODO: better name
class BaseUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(BaseUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'vorname', 'nachname', 'eingeladen_von', 'telefonnummer']
        # widgets = [
        #     'username', forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'hans.peter'}),
        #     'vorname', forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Hans'}),
        #     'nachname', forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Peter'}),
        #     'telefonnummer', forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': '015718769187'}),
        #     'password1', forms.PasswordInput(attrs={
        #         'class': 'form-control'}),
        #     'password2', forms.PasswordInput(attrs={
        #         'class': 'form-control'}),
        # ]

# TODO: better name
class BaseUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ['vorname', 'nachname']
