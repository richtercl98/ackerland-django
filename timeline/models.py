from django.db import models

# credit user model abstraction: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    vorname = models.CharField(max_length=64, null=True, blank=True)
    nachname = models.CharField(max_length=64, null=True, blank=True)
    bezahlt = models.BooleanField(default=False)


class Floor(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return "{}".format(self.name)

class DiscJockey(models.Model):
    pseudonym = models.CharField(max_length=64)
    bio = models.URLField(max_length=1024, null=True, blank=True)

    # human readable respresentation in admin site
    def __str__(self):
        return "{}".format(self.pseudonym)


class Timeslot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    genre = models.CharField(max_length=128, null=True, blank=True)

    location = models.OneToOneField(Floor, on_delete=models.CASCADE)
    acts = models.ManyToManyField(DiscJockey)

    def __str__(self):
# represent Timeslot in following human readable form: Floor: 00:00 - 02:00
        return "{floor}: {start:%H:%M} - {end:%H:%M}".format(
            floor = self.location,
            start = self.start_time,
            end = self.end_time)

    class Meta:
        ordering = ['location', 'date', 'start_time']
