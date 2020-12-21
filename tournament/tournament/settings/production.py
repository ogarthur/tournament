from __future__ import absolute_import, unicode_literals
from tournament.settings.base_settings import *
import os

env = os.environ.copy()
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')



DEBUG = False
#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('BD_NAME'),
        'USER':  os.environ.get('BD_USER'),
        'PASSWORD': os.environ.get('BD_PASS'),
        'HOST': os.environ.get('BD_HOST'),
        'PORT': os.environ.get('BD_PORT'),
    }
}
# Allow all host headers
ALLOWED_HOSTS = ['*',]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
