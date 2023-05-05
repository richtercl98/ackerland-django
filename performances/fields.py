from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models

class MultiURLField(models.CharField):
    description = "A field that can contain multiple URLs, separated by commas"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(self.validate_urls)

    def validate_urls(self, value):
        if value is None or value.strip() == '':
            return
        urls = value.split(',')
        url_validator = URLValidator()
        for url in urls:
            try:
                url_validator(url.strip())
            except ValidationError:
                raise ValidationError('Invalid URL: {}'.format(url.strip()))
