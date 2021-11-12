# config/settings/production.py
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# allowed hosts
ALLOWED_HOSTS = []

# Django Rest Framework CORS configuration
# cors origin whitelist
CORS_ORIGIN_WHITELIST = ()

# AWS Acces Keys
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID_PROD')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY_PROD')
