"""
Django settings for ackerland project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# credit: https://saralgyaan.com/posts/best-way-to-start-a-django-project-with-github-integration/
from decouple import config
# credit: https://pypi.org/project/Django-Verify-Email/
from django.core.mail import send_mail

SECRET_KEY = config('SECRET_KEY')

LOGIN_REDIRECT_URL = 'ticketstatus'
LOGOUT_REDIRECT_URL = 'home'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)
#DEBUG = False

ALLOWED_HOSTS = [
'168.119.182.218',
'talu-festival.de',
'www.talu-festival.de',
'localhost',
'127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Installed third party Apps
    'phonenumber_field',
    'verify_email.apps.VerifyEmailConfig',  # credit: https://pypi.org/project/Django-Verify-Email/

    # My Apps
    #'timeline', # credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
    'accounts',
    'faq',
    'performances',
]
# credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Fix bug in call of reverse() when new registrated user click on verification link
LOGIN_URL = 'home'
LOGIN_REDIRECT_URL = 'home'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
 #   'django.contrib.admin.middleware.AdminMiddleware',
     # credit:https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail
#    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'ackerland.urls'

# credit: https://pypi.org/project/Django-Verify-Email/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)
EMAIL_HOST_USER = config('EMAIL_ID')
EMAIL_HOST_PASSWORD = config('EMAIL_PW')

DEFAULT_FROM_EMAIL = config('EMAIL_ID')

VERIFICATION_SUCCESS_TEMPLATE = "../static/custom_verification_success.html"
HTML_MESSAGE_TEMPLATE = "../static/verification_mail.html"
#VERIFICATION_SUCCESS_TEMPLATE = None


PHONENUMBER_DEFAULT_REGION = 'DE'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # credit: https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
        # 'DIRS': [os.path.join(BASE_DIR, 'templates'),
        # os.path.join(BASE_DIR, 'ackerland-frontend')],      # In diesen Verzeichnissen sucht django nach HTML-Templates
        'DIRS': [
                os.path.join(BASE_DIR, 'static'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ackerland.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if config('production', cast=bool):
    # Database settings on hetzner server
    # print('production')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'taludb',
    	'USER': 'taludbuser',
    	'PASSWORD': 'taludbuser_password',
    	'HOST': 'localhost',
    	'PORT': '',
        },
    }

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'ackerland-frontend/app'),  # in diesen Verzeichnissen sucht manage.py collectstatic nach Statischen Dateien
        os.path.join(BASE_DIR, 'ackerland-frontend/talu_verification_mail'),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
else:
    # print('DEVELOPMENT')
    # Database settings in development
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        }
    }

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'ackerland-frontend/app'),  # in diesen Verzeichnissen sucht manage.py collectstatic nach Statischen Dateien
        os.path.join(BASE_DIR, 'ackerland-frontend/talu_verification_mail'),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')     # hier werden von manage.py collectstatic gesammelten Statische Dateien gespeichert

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'de-ger'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


TIME_INPUT_FORMATS = [
    '%H:%M',        # '14:30'
]

# Pfad aus dem Static files zurückgegeben werden (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
