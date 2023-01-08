from django.contrib import admin

# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms.userforms import BaseUserCreationForm, BaseUserChangeForm
from .models import User, Guest, Orga, Volunteer, Artist, Technician

class BaseUserAdmin(UserAdmin):
    add_form = BaseUserCreationForm
    form = BaseUserChangeForm
    model = User
    list_display = '__all__'
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('vorname', 'nachname', 'bezahlt')}),
    ) #this will allow to change these fields in admin module


admin.site.register(User, UserAdmin)
admin.site.register(Guest)
admin.site.register(Orga)
admin.site.register(Volunteer)
admin.site.register(Artist)
admin.site.register(Technician)
