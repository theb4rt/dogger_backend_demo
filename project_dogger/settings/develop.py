"""Config file for development b4rt"""
# config/settings/develop.py
import os
from .common import *

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Django Rest Framework CORS configuration
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]


#AWS ACCES KEYS
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID_DEV',default='secret_acces_key')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY_DEV',default="secret_key")

# Application definition

THIRD_PARTY_APPS_DEVELOP = (
)

INSTALLED_APPS += THIRD_PARTY_APPS_DEVELOP


