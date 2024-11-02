"""
Django settings for export_homecare project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path,os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r$^0y4ht1p&&7o$7ham*3f_bw$f-asm02xa*q0m!nn@%$z1dgx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['miniproject-s9.onrender.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'customerlogin',
    'custadmin',
    'employee',
    'customserviceprovider',
    'django.contrib.staticfiles',

    'social_django',
    # 'mainApp',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

AUTHENTICATION_BACKENDS = (
   'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.google.GoogleOAuth2', 
     'customerlogin.backends.CustomUserBackend', 
      
)

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional' 


SITE_ID = 1


LOGIN_URL = 'login1'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'us'
# LOGOUT_REDIRECT_URL = '/'

# LOGIN_URL='login1'
LOGIN_REDIRECT_URL = 'userloginhome'

# Google OAuth2 settings
# settings.py

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH2_PROVIDER_URLS': {
          'google': 'https://accounts.google.com/o/oauth2/auth',
        },
        'PROVIDER_AUTH_PARAMS': {
            'google': {
                'prompt': 'select_account',
            },
        },
        'OAUTH2_SCOPE': [
            'email',
            'profile',
        ],
        'OAUTH2_CLIENT_ID': '460530869371-0h00c12mguoc108evtbl0mdg4rk9spnl.apps.googleusercontent.com',
        'OAUTH2_SECRET': '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',
         'OAUTH2_REDIRECT_URI': 'http://127.0.0.1:8000/auth/complete/google-oauth2/',
    }
}


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY  = '460530869371-0h00c12mguoc108evtbl0mdg4rk9spnl.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile']






MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
      'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'export_homecare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'export_homecare.wsgi.application'

# MEDIA_URL = 'media/'

# # Define the path to the media directory
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# DATABASES = {
#   'default': {
#         'ENGINE': 'mysql.connector.django',
#         'NAME': 'your_database_name',
#         'HOST': 'localhost',  # Or your database host
#         'PORT': '3306',       # Or your database port
#         'USER': '',           # Empty username
#         'PASSWORD': '',
# }
# }
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

import os
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# URL to access static files
STATIC_URL = '/static/'

# Directory for static files in development
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Directory where static files will be collected for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise storage setting for production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mathewpeter2025@mca.ajce.in'
EMAIL_HOST_PASSWORD = 'kattimattathil@8'

# Add these settings in your settings.py
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
AUTH_USER_MODEL = 'customerlogin.Customer'




# settings.py

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
     
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'customerlogin.auth_pipeline.social_user_custom',  # Custom social user step
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'customerlogin.auth_pipeline.save_profile',  # Custom function to handle profile saving
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

# Ensure you have your custom user model configured
AUTH_USER_MODEL = 'customerlogin.Customer'
