"""
WSGI config for ackerland project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# credit: https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail
# from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ackerland.settings')

application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
