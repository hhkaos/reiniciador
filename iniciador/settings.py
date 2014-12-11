"""
Django settings for iniciador project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!

LOGIN_REDIRECT_URL = '/members/profile/'
LOGOUT_URL = '/'

try:
    from local_settings import *
except ImportError as e:
    pass

#EMAIL ADDRESS
FROM_EMAIL = "gerencia@iniciador.com"

if DEBUG:
    SERVER = 'localhost:8000'
else:
    SERVER = 'reiniciador.com'

ALLOWED_HOSTS = ('reiniciador.com',)


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
)

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

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'

USE_I18N = True
USE_L10N = True
USE_TZ = True

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
