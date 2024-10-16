"""
Django settings for right_way_realty project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from typing import Dict, Any
# import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$tp%#7shjbl-f*-74%xez$#2+&@c6^k*65d*w^!%bcvvq3n0!_"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    'django.contrib.humanize',
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "phonenumber_field",
    "app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "right_way_realty.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

#Celery  tasks
CELERY_BROKER_URL = 'redis://localhost:6379/0' 
CELERY_BEAT_SCHEDULE = {
    'fetch-navica-data-every-10-minutes': {
        'task': 'app.tasks.fetch_navica_data_task',
        'schedule': 600.0, 
    },
}

WSGI_APPLICATION = "right_way_realty.wsgi.application"

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "ramolaryan@gmail.com"
EMAIL_HOST_PASSWORD = "qmmt agec ghzl meip"
# DEFAULT_FROM_EMAIL = "your-email@example.com"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


if 'HEROKU' in os.environ:
    DATABASES = {'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', 'postgres://ufffrdilmdrd4v:p222e9d6f3b11fff1458e2b96e933c0d6c6cbff6eca818d7434c11f8b3dfd0a93@cd1goc44htrmfn.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d212e6j0gdrt09')
    )
    }

else:
    DATABASES = {
        'default':{
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'right-way-realty',  # Name of your local database
            'USER': 'postgres',  # PostgreSQL username
            'PASSWORD': 'admin',  # PostgreSQL password
            'HOST': 'localhost',
            'PORT': '5432',  # Default PostgreSQL port
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

GOOGLE_API_KEY = "YOUR_KEY"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

# Media files (images, etc..)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# STATIC_URL = "app/static/"


# MEDIA_URL = 'app/images/'

# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Initialize environment variables
# env = environ.Env()
# # Read .env file (optional, for local development)
# environ.Env.read_env()

# # Set your secret key and debug flag using environment variables
# SECRET_KEY = env('SECRET_KEY')
# DEBUG = env.bool('DEBUG', default=False)

# # Use environment variables for your API keys
# GOOGLE_MAPS_API_KEY = env('GOOGLE_MAPS_API_KEY')
# FLEXMLS_API_KEY = env('FLEXMLS_API_KEY')
