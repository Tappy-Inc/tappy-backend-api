"""
Django settings for tappy project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import sys

# Library: django-environ
import environ

# Library: djangorestframework-simplejwt
import datetime

# Logging
import logging

# Logging
logger = logging.getLogger(__name__)

# Library: django-environ
env = environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG')

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

# To have an option to disable logging
if '--no-logs' in sys.argv:
    print('> Disabling logging levels of CRITICAL and below.')
    sys.argv.remove('--no-logs')
    logging.disable(logging.CRITICAL)

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Library: djangorestframework
    'rest_framework',
    # Library: drf-yasg
    'drf_yasg',
    # Library: django-cors-headers
    'corsheaders',
    # Library: django-simple-history
    'simple_history',
    # Library: django-unfold
    # Notes: It is necessary to have new option before django.contrib.admin to be sure it will be properly loaded, 
    # otherwise it is possible to get unexpected errors.
    "unfold",
    'django.contrib.admin',
    # Library: django-storages
    'storages',
    # Library: django-filter
    'django_filters',
    # Domain
    'domain.common',
    'domain.system',
    'domain.user',
    'domain.memphis',
    'domain.mailer',
    # API
    'api.system_management',
    'api.user_management',
    'api.authenticated',
    'api.employee',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Library: django-log-request-id
    'log_request_id.middleware.RequestIDMiddleware',
    # Library: django-cors-headers
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Library: django-simple-history
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'tappy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'tappy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DB_ENGINE'),
        'NAME': os.environ.get('DJANGO_DB_NAME'),
        'USER': os.environ.get('DJANGO_DB_USER'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASS'),
        'HOST': os.environ.get('DJANGO_DB_HOST'),
        'PORT': os.environ.get('DJANGO_DB_PORT'),
        # NOTE: Comment this if not using Vercel Database
        # 'CONN_MAX_AGE': 0,
        # 'CONN_HEALTH_CHECKS': True,
        'OPTIONS': {
            'sslmode': 'require',
            # 'options': f"endpoint={os.environ.get('DJANGO_DB_ENDPOINT')}", # NOTE: Uncomment this if using Vercel Database

        } if os.environ.get('DJANGO_ENV') != 'local' else {}
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = f"{os.environ['S3_BUCKET_URL']}/static/"
STATIC_ROOT = 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Library: django-log-request-id
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['request_id'],
            'formatter': 'standard',
            'level': 'DEBUG',
        },
    },
    'filters': {
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter'
        },
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)-8s [%(asctime)s] [%(request_id)s] %(name)s: %(message)s'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Library: djangorestframework-simplejwt
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=60)
}

# Library: djangorestframework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # Library: djangorestframework-simplejwt
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # Library: django-filter
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # Library: djangorestframework
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}

# Library: drf-yasg
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        # 'Basic': {
        #       'type': 'basic'
        # },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
FORCE_SCRIPT_NAME = '/'

# Library: django-cors-headers
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = ['*']

# Library: django-storages
AWS_S3_SIGNATURE_VERSION = 's3v4'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = env('DO_SPACES_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = env('DO_SPACES_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = env('DO_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = env('DO_SPACES_URL')
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=300',}
AWS_LOCATION = env('DO_LOCATION')

# Django: abstract-user
AUTH_USER_MODEL = "domain_user.User"