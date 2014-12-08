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

#'''Heroku conf'''
# Parse database configuration from $DATABASE_URL
#import dj_database_url
try:
    from local_settings import *
except ImportError as e:
    pass

#DATABASES = {}
#DATABASES['default'] =  dj_database_url.config()

#EMAIL ADDRESS
FROM_EMAIL = "gerencia@iniciador.com"
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'iniciador_db',
        'USER': 'reiniciador',
        'PASSWORD': 'yoemprendo',
        'HOST': '',
        'PORT': '5432',
    }
}
SERVER = 'himan.webfactional.com'

'''
    #SERVER = 'iniciador.herokuapp.com'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#'''END Heroku conf'''

ALLOWED_HOSTS = ('himan.webfactional.com',)


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
'''STATIC_ROOT = '/home/himan/webapps/static_media/'
STATIC_URL = '/static/'''


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
