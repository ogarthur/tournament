from __future__ import absolute_import, unicode_literals
from tournament.settings.base_settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tournament_db',
        'USER': 'django_user',
        'PASSWORD': 'django_pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [ '*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from dashboard.base_settings import *
except ImportError:
    pass
