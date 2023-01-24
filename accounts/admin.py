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
    list_display = ['vorname', 'nachname', 'email', 'telefonnummer', 'eingeladen_von']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('vorname', 'nachname', 'telefonnummer', 'eingeladen_von')}),
    ) #this will allow to change these fields in admin module


class GuestAdmin(admin.ModelAdmin):
    list_display = ['user', 'bezahlt']
    # fieldsets = admin.ModelAdmin.fieldsets + ((None, {'fields' : ('user', 'bezahlt')}),)
admin.site.register(User, BaseUserAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Orga)
admin.site.register(Volunteer)
admin.site.register(Artist)
admin.site.register(Technician)
