"""
Django settings for syu_clubs_api_server project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g7nf!xaqekwki@mwa(u5yyqo!z%)0t84&6x)xcv#_owh5(m+=b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

from secure import env
# from . import env
credential_path = "secure/syuClubs-secure.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

DEFAULT_FILE_STORAGE = 'syu_clubs_api_server.gcloud.GoogleCloudMediaFileStorage'
# STATICFILES_STORAGE = 'syu_clubs_api_server.gcloud.GoogleCloudStaticFileStorage'

GS_PROJECT_ID = env.MY_PROJECT_ID

# GS_STATIC_BUCKET_NAME = env.MY_STATIC
GS_MEDIA_BUCKET_NAME = env.MY_MEDIA

# STATIC_URL = 'https://storage.googleapis.com/{}/'.format(GS_STATIC_BUCKET_NAME)
# STATIC_ROOT = "static/"

GS_ACCESS_KEY_ID= env.MY_ACCESS_ID
GS_SECRET_ACCESS_KEY = env.MY_SECRET_KEY

MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_MEDIA_BUCKET_NAME)

UPLOAD_ROOT = 'media/uploads/'

# DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
# DOWNLOAD_URL = STATIC_URL + "media/downloads"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'user',
    'clubs',
    'posts',
    'common',

    'rest_framework',
    'corsheaders',
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

ROOT_URLCONF = 'syu_clubs_api_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 템플릿 위치를 client 폴더로 고정 
        'DIRS': ['client'],
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

WSGI_APPLICATION = 'syu_clubs_api_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
import platform

platform = platform.platform()
if platform == "Linux-4.19.76-linuxkit-x86_64-with-glibc2.2.5":
    DATABASES = { 
        'default' : {
            'ENGINE' : 'django.db.backends.mysql',
            'HOST' : '10.10.0.2',
            'OPTIONS' : {
                'read_default_file' : os.path.join(PROJECT_ROOT, './secure/mysql.cnf'),
                'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }
else :
    DATABASES = { 
        'default' : {
            'ENGINE' : 'django.db.backends.mysql',
            'HOST' : '127.0.0.1',
            'OPTIONS' : {
                'read_default_file' : os.path.join(PROJECT_ROOT, './secure/mysql.cnf'),
                'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }



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

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATICFILES_DIRS = [
    # 실제 static 파일은 모두 client 측에서 소유 
    os.path.join(PROJECT_ROOT, 'client/static/')
]

CORS_ORIGIN_ALLOW_ALL = True 
CORS_ALLOW_CREDENTIALS = True
