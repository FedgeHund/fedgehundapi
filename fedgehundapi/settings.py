"""
Django settings for fedgehundapi project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ

env = environ.Env()

# reading .env file
environ.Env.read_env()

DJANGO_ENV = env("ENV", default="development")

# SECURITY WARNING: don't run with debug turned on in production!
if DJANGO_ENV == "production":
    DEBUG = True  # Change this to false when deploying final app
else:
    DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DJANGO_ENV == "production":
    # Use hosted remote DB in production
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': env("PRODUCTION_DB_NAME"),
            'CLIENT': {
                'host': env("HOST_IP"),
                'port': int(env("HOST_PORT")),
                'username': env("PRODUCTION_DB_USERNAME"),
                'password': env("PRODUCTION_DB_PASSWORD"),
                'authSource': env("PRODUCTION_DB_NAME"),
            },
        }
    }
else:
    # Use local DB in development
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': env('LOCAL_DB_NAME', default=''),
        }
    }

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'SECRET_KEY', default='f9y!yh1nb6lm5(o*)^(8+-dueu9_p=p$c$d-u8f(p=w+mtd%rx')

ALLOWED_HOSTS = ['MrktDB.eba-brufwk2z.us-west-2.elasticbeanstalk.com','127.0.0.1','www.mrktdb.com', 'localhost']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

CORS_ORIGIN_WHITELIST = [
    'http://www.mrktdb.com',
    'http://mrktdb.eba-brufwk2z.us-west-2.elasticbeanstalk.com',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://localhost:3000',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    # django rest framework
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    
    # for social login
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    # Apps
    'fedgehund_auth',
    'fedgehund_profile.apps.FedgehundProfileConfig',
    'edgar.apps.EdgarConfig',
    'filer.apps.FilerConfig',
    'testapp',
    'holdings.apps.HoldingsConfig',
    'fedgehundui',
    'django_cron',
    'security.apps.SecurityConfig'
]

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
# The username field is optional and we will hide it in the registration page
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            "client_id": "697434274174-b3jeg526rn1da2vrn3si3d9or0t2c3to.apps.googleusercontent.com",
            "secret": "oLkjadkLRhQppydlIDF856cS",
            "key": ""
        },
        # These are provider-specific settings that can only be
        # listed here:
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    }
}

SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = True


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fedgehundapi.urls'

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

WSGI_APPLICATION = 'fedgehundapi.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

CRON_CLASSES = [
    "edgar.cikCusipCronJob.CikCusipCronJob",
    "edgar.securityLinkCompanyCronJob.SecurityLinkCompanyCronJob",
    "edgar.cusipTickerMappingSecurityUpdate.CusipTickerMappingSecurityUpdate"
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'root': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True
        },
        'console_logger': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True
        }
    }
}
