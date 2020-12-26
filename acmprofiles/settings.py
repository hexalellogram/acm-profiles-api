"""
Django settings for acmprofiles project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# from https://devcenter.heroku.com/articles/django-assets
# the below line causes tests to fail
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).par

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'profiles',
    'rest_framework',
    'django.contrib.postgres',
    'drf_yasg',
]

MIDDLEWARE = [
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'profiles.middleware.AuthenticationMiddleware'
]

ROOT_URLCONF = 'acmprofiles.urls'

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

WSGI_APPLICATION = 'acmprofiles.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#intructions for setting up Postgres
# download here https://www.postgresql.org/download/
# pipenv install
# pipenv shell
# su OSuser_here
# createuser -dP db_new_local_username_here (will prompt to enter new password)
# createdb -E utf8 -U username new_local_db_name_here

# postgres://user:password@host:port/database_name
db = os.environ["DATABASE_URL"][11:]
ind = db.index(":")
user = db[:ind]
db = db[ind+1:]
ind = db.index("@")
password = db[:ind]
db = db[ind+1:]
ind = db.index(":")
host = db[:ind]
db = db[ind+1:]
ind = db.index("/")
port = db[:ind]
name = db[ind+1:]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': name, #db_name
        'USER': user, #local_username
        'PASSWORD': password, #local password
        'HOST': host,
        'PORT': port
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = '/static/'

# from https://devcenter.heroku.com/articles/django-assets
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SWAGGER_SETTINGS={
    'SECURITY_DEFINITIONS':{
        "Auth token eg [Bearer (JWT) ]":{
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}
