# config/settings/testing.py
import os

from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']

THIRD_PARTY_APPS_TESTING = (
    'django_extensions',
    'speedinfo',
)

INSTALLED_APPS += THIRD_PARTY_APPS_TESTING

# Django Rest Framework CORS configuration
CORS_ORIGIN_ALLOW_ALL = True
