import os

from drf_boilerplate.settings.loader import load_credential

ENV_SETTINGS_MODE = os.getenv('SETTING_MODE')

if ENV_SETTINGS_MODE == 'prod':
    from .production import *
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backend.mysql',
            'HOST': load_credential('PROD_DATABASE_HOST'),
            'NAME': load_credential('PROD_DATABASE_NAME'),
            'USER': load_credential('PROD_DATABASE_USER'),
            'PASSWORD': load_credential('PROD_DATABASE_PASSWORD'),
        }
    }
else:
    from .local import *
    # local
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': 'localhost',
            'NAME': 'drf_boilerplate',
            'USER': 'root',
            'PASSWORD': 'somniholic.mathpresso'
        }
    }