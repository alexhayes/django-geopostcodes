# -*- coding: utf-8 -*-
"""
    module.name
    ~~~~~~~~~~~~~~~
    Preamble...
"""
from __future__ import absolute_import, print_function, unicode_literals

# TEST SETTINGS
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Django replaces this, but it still wants it. *shrugs*
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.gis',
    'django_geopostcodes',
)

MIDDLEWARE_CLASSES = {}

NOSE_ARGS=[
    '--logging-clear-handlers',
    # Coverage - turn on with NOSE_WITH_COVERAGE=1
    '--cover-html',
    '--cover-package=django_geopostcodes',
    '--cover-erase',
    '--with-fixture-bundling',
    # Nose Progressive
    '--with-progressive',
]

SECRET_KEY = '53cr3773rc3553cr3773rc3553cr3773rc3553cr3773rc35'

