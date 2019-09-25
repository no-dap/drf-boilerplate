from drf_boilerplate.settings.loader import load_credential
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

# AWS SETTINGS

AWS_ACCESS_KEY_ID = load_credential('AWS_S3_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = load_credential('AWS_S3_SECRET_ACCESS_KEY')

AWS_REGION = 'ap-northeast-2'  # Seoul Region
AWS_STORAGE_BUCKET_NAME = 'weird-competition'
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_S3_SECURE_URLS = True  # https

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN

MEDIA_BUCKET_NAME = 'weird-competition-media'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % MEDIA_BUCKET_NAME
MEDIA_URL = 'https://%s/' % MEDIA_S3_CUSTOM_DOMAIN
# END AWS SETTINGS
