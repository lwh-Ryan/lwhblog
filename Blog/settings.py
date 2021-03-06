"""
Django settings for Blog project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
#from local_settings import debug, storage
from local_settings import DB_USER, DB_PASSWORD, QN_ACCESS_KEY, QN_SECRET_KEY, debug
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8-2=j0c!gm(49u2$jd!hfdhcirw)3mulxw46@j0%@m1l6zf+uy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', ]
#'yumendy.com', 'www.yumendy.com'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website.apps.WebsiteConfig',
    'navbar.apps.NavbarConfig',
    'authentication.apps.AuthenticationConfig',
    'article.apps.ArticleConfig',
    'link.apps.LinkConfig',
    'mood.apps.MoodConfig',
    'DjangoUeditor',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Blog.wsgi.application'

from local_settings import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

'''if storage == 'qiniu':
    from local_settings import QN_SECRET_KEY, QN_ACCESS_KEY, QN_BUCKET_NAME, QN_BUCKET_DOMAIN

    STATIC_URL = 'http://odblm5gk0.bkt.clouddn.com/static/'
    MEDIA_URL = 'http://odblm5gk0.bkt.clouddn.com/media/'
    DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'
    STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'
    QINIU_ACCESS_KEY = QN_ACCESS_KEY
    QINIU_SECRET_KEY = QN_SECRET_KEY
    QINIU_BUCKET_NAME = QN_BUCKET_NAME
    QINIU_BUCKET_DOMAIN = QN_BUCKET_DOMAIN
else:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/' '''
STATIC_URL = 'http://oc2ae6w67.bkt.clouddn.com/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')

MEDIA_URL = 'http://odblm5gk0.bkt.clouddn.com/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

QINIU_ACCESS_KEY = QN_ACCESS_KEY
QINIU_SECRET_KEY = QN_SECRET_KEY
QINIU_BUCKET_NAME = 'yumendy-blog'
QINIU_BUCKET_DOMAIN = 'oc2ae6w67.bkt.clouddn.com'
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'
STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'   

STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

LOG_FILE = os.path.join(BASE_DIR, 'log/blog.log')
DEBUG_LOG_FILE = os.path.join(BASE_DIR, 'log/debug.log') 

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] %(module)s : %(message)s'
        },
        'verbose': {
            'format': '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s'
        }
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'filters': ['require_debug_true', 'require_debug_false']
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': LOG_FILE,
            'mode': 'a',
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': DEBUG_LOG_FILE,
            'mode': 'a',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}