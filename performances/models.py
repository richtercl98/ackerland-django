from django.db import models

from accounts.models import User
# Create your models here.

class Act(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    genre = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/')
    sound_sample_url = models.URLField(blank=True)
    corresponding_users = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return self.name

class Workshop(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    max_participants = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    corresponding_users = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return self.name
