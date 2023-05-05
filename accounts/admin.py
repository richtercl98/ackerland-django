from django.contrib import admin

# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms.userforms import BaseUserCreationForm, BaseUserChangeForm
from .models import User, Guest, Orga, Volunteer, Artist, Technician

@admin.action(description='Mark selected Users as bezahlt')
def make_payment_status_bezahlt(modeladmin, request, queryset):
    queryset.update(bezahlt=True)

class BaseUserAdmin(UserAdmin):
    add_form = BaseUserCreationForm
    form = BaseUserChangeForm
    model = User
    list_display = ['vorname', 'nachname', 'bezahlt', 'email','eingeladen_von']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('vorname', 'nachname', 'bezahlt', 'eingeladen_von')}),
    ) #this will allow to change these fields in admin module

    actions = [make_payment_status_bezahlt]

    def bezahlt_user_count(self, obj):
        return User.objects.filter(bezahlt=True).count()

    bezahlt_user_count.short_description = "Anzahl Bezahlungen"

    def income_count(self, obj):
        return User.objects.filter(bezahlt=True).count() * 25

    income_count.short_description = "Gesamtbudget"
# class GuestAdmin(admin.ModelAdmin):
    # list_display = ['user', 'bezahlt']
    # fieldsets = admin.ModelAdmin.fieldsets + ((None, {'fields' : ('user', 'bezahlt')}),)
admin.site.register(User, BaseUserAdmin)
admin.site.register(Guest)
admin.site.register(Orga)
admin.site.register(Volunteer)
admin.site.register(Artist)
admin.site.register(Technician)
