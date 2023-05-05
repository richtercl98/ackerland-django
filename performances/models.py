from django.db import models

from accounts.models import User

from .fields import MultiURLField
# Create your models here.

class Act(models.Model):
    stage_name = models.CharField(max_length=64)
    description = models.CharField(max_length=400)
    genre = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to='static/img/acts/')
    sound_sample_url = models.URLField(max_length=256, blank=True)
    insta_url = models.URLField(max_length=256, blank=True)
    corresponding_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, unique=False)

    def __str__(self):
        return self.stage_name

class Workshop(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=300)
    max_participants = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    corresponding_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, unique=False)
    image = models.ImageField(upload_to='static/img/workshops/', default=None)

    def __str__(self):
        return self.name
