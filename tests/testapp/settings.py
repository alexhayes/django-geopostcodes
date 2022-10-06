# -*- coding: utf-8 -*-
"""
    tests.testapp.settings
    ~~~~~~~~~~~~~~~~~~~~~~

    Django settings for tests.
"""
import os

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Django replaces this, but it still wants it. *shrugs*
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('TEST_DB_NAME', 'django_geopostcodes_test'),
    }
}

if os.environ.get('TEST_DB_USER', None):
    DATABASES['default']['USER'] = os.environ.get('TEST_DB_USER')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.gis',
    'django.contrib.messages',
    'django_geopostcodes',
)

MIDDLEWARE_CLASSES = {}

SECRET_KEY = '53cr3773rc3553cr3773rc3553cr3773rc3553cr3773rc35'

try:
    GDAL_LIBRARY_PATH = os.environ['GDAL_LIBRARY_PATH']
except KeyError:
    pass

try:
    GEOS_LIBRARY_PATH = os.environ['GEOS_LIBRARY_PATH']
except KeyError:
    pass

try:
    SPATIALITE_LIBRARY_PATH = os.environ['SPATIALITE_LIBRARY_PATH']
except KeyError:
    pass

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ]
        },
    }
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

USE_TZ = True
