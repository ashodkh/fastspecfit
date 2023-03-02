#!/usr/bin/env python

"""Django settings for FastSpecFit project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/

"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# This is the "webapp" dir.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

USER_QUERY_DIR = '/user-uploads'

# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'eok&i&(7=!8u%9lr48%pks9x7pfp7b=a6^p)^ldscte+t&_tz+')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',
                 'testserver',
                 'fastspecfit.desi.lbl.gov',
                 'fastspecfit.legacysurvey.org',
                 ]

# Application definition

INSTALLED_APPS = [
    'django_filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fastspecfit.webapp.fastmodel',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fastspecfit.webapp.urls'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

WSGI_APPLICATION = 'fastspecfit.webapp.wsgi.application'

if DEBUG:
    import logging
    l = logging.getLogger('django.db.backends')
    l.setLevel(logging.DEBUG)
    l.addHandler(logging.StreamHandler())

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db', 'db.sqlite3'),
#    }
#}

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'fastspecfit',
       'USER': 'fastspecfit',
       'PASSWORD': os.environ.get('POSTGRES_DB_PASSWORD'),
       'HOST': 'db-loadbalancer.cosmo-fastspecfit.production.svc.spin.nersc.org',
   }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

#python manage.py check --deploy recommended settings

#SECURE_HSTS_SECONDS =
#SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
#SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
#X_FRAME_OPTIONS = 'DENY'
