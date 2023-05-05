from django.db import models

from accounts.models import User

from .fields import MultiURLField
# Create your models here.

class Act(models.Model):
    stage_name = models.CharField(max_length=64)
    description = models.CharField(max_length=400)
    genre = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to='images/')
    sound_sample_urls = MultiURLField(max_length=256, blank=True)
    insta_url = models.URLField(max_length=256, blank=True)
    corresponding_users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

class Workshop(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=300)
    max_participants = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    corresponding_users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name
