"""
Django settings for authorization project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^gubycj@0fk)h5^1&=^497c8#=&d2lh9nb2=8z_h-y@616x%(t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
AUTHENTICATION_BACKENDS = [
    # "django.contrib.auth.backends.ModelBackend",
    'authorization.authentication_backend.KeycloakAuthBackend'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


ROOT_URLCONF = 'authorization.urls'

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

WSGI_APPLICATION = 'authorization.wsgi.application'

KEYCLOAK_ACCESS_TOKEN_NAME = "keycloak_access"
KEYCLOAK_REFRESH_TOKEN_NAME = "keycloak_refresh"

KEYCLOAK_CONFIG = {
    "SERVER_URL": "http://localhost:8080/auth/",
    "CLIENT_ID": "authentication_exchange",
    "REALM_NAME": "users",
    "CLIENT_SECRET_KEY": "teUmxsXzqSxcizyrns9UlE248bMMkr3B",
    "PUBLIC_KEY": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtkWzx9SzArE761rlCtJ0EElEdZylFz3Y1GLS2K4rAFIV5NpyoijahsZ3dx6RJZTzNJLH8hnvKLaot7iLIhXby7wWA59T2FiWgZ3VWUuqMrfjELAcfaXwG7WwJC2H88VOLmIHPt9+kHNDk5UvR/UPJn3j7EtMSP7Uv/l3ksQX6zPXGgome0IcuuLi3Wa4utLV4j37pGhRmNQsNnIS94pBlpZiOPiDASE+7GEKD6aroHHSHr6IhfcG+b/g8nv57fj1rOB8YfgPG3SFCOKfT5dkwWNMcb+N7LZo09ga8lRJ4+5TnLuOYptnd8nLNj8Z7LfLzNNOkSAEHFzO7IdkUgS9BQIDAQAB",
    "AUTHORIZATION_CONFIG": os.getcwd()+'/src/authorization/authorization-config.json',
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
