# config/settings/staging.py
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# allowed hosts
ALLOWED_HOSTS = ['*']

# Django Rest Framework CORS configuration
# cors origin whitelist
CORS_ORIGIN_ALLOW_ALL = True

