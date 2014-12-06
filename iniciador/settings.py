"""
Django settings for iniciador project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+ax-x$vcc4)#w^c#+5=kdbv8buz@81g9w018g0(o!t+nlyj012'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
LOGIN_REDIRECT_URL = '/members/profile/'
LOGOUT_URL = '/'

'''Heroku conf'''
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

#EMAIL ADDRESS
FROM_EMAIL = "gerencia@iniciador.com"

if DATABASES['default'] == {}:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'iniciador_local',
            'USER': 'iniciador_local',
            'PASSWORD': '123456',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
    SERVER = 'localhost:8000'
else:
    SERVER = 'iniciador.herokuapp.com'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
'''END Heroku conf'''

ALLOWED_HOSTS = ('*',)


# Application definition

INSTALLED_APPS = (
    #'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members',
    'djrill',
    'rest_framework',
    #'storages',
)

MANDRILL_API_KEY = "vUb8YeytJCcpZqbeaPnYKQ"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'iniciador.urls'

WSGI_APPLICATION = 'iniciador.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
'''
Remove by heroku
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'

USE_I18N = True
USE_L10N = True
USE_TZ = True

'''
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
'''

#Amazon S3
'''
DEFAULT_FILE_STORAGE = 'libs.storages.S3Storage.S3Storage'
AWS_ACCESS_KEY_ID =
AWS_SECRET_ACCESS_KEY =
AWS_STORAGE_BUCKET_NAME =
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
'''


# New heroku
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# End heroku
MEDIA_URL = os.path.join(BASE_DIR, 'media/')
ADMIN_MEDIA_PREFIX = '/media/'

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
