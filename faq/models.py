from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class LowerCaseCharField(models.CharField):
# credit: https://stackoverflow.com/questions/36330677/django-model-set-default-charfield-in-lowercase
    def get_prep_value(self, value):
        return str(value).lower()

class Faq(models.Model):
    topic = models.CharField(max_length=32, null=False, blank=False)
    text = models.TextField()
    custom_order = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.topic
