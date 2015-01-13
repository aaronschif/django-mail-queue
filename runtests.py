#!/usr/bin/env python

import os, sys
from django.conf import settings
import django

DIRNAME = os.path.dirname(__file__)

django_settings = {
    'DEBUG': True,
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    'ROOT_URLCONF': 'mailqueue.urls',
    'INSTALLED_APPS': (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'mailqueue',
    ),
    'MIDDLEWARE_CLASSES': (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ),
    'USE_TZ': True
}

if django.VERSION[1] < 4:
    # If the version is NOT django 4 or greater
    # then remove the TZ setting.

    django_settings.pop('USE_TZ')

settings.configure(**django_settings)


try:
    # Django 1.7 needs this, but other versions dont.
    django.setup()
except AttributeError:
    pass

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['mailqueue', ])
if failures:
    sys.exit(failures)
