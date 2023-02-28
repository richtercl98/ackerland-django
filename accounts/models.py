from django.db import models

# credit user model abstraction: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/

from django.contrib.auth.models import AbstractUser

# credit: https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#model-field
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    vorname = models.CharField(max_length=64, null=True, blank=True)
    nachname = models.CharField(max_length=64, null=True, blank=True)
    telefonnummer = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=256)

    bezahlt = models.BooleanField(default=False)

    eingeladen_von = models.ForeignKey('Orga', on_delete=models.SET_NULL, null=True, related_name='eingeladen_von')

    def __str__(self):
        return '{} {}'.format(self.vorname, self.nachname)

class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.vorname, self.user.nachname)

class Orga(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.vorname, self.user.nachname)

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.vorname, self.user.nachname)

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.vorname, self.user.nachname)


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.vorname, self.user.nachname)
