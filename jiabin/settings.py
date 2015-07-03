"""
Django settings for mengup project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import os.path
import sys

reload(sys) 
sys.setdefaultencoding("utf-8") 
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p70=r*%67#7--0jm23a_d3$ny)*x=p1+w_15udzfsdm8rpm*dn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


HERE = os.path.dirname(os.path.abspath(__file__)) 
HERE = os.path.join(HERE,'../') 
# Application definition
ROOT_URLCONF = 'mengup.urls'

WSGI_APPLICATION = 'mengup.wsgi.application'


INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'django.contrib.sites',
    'app_pc',
    'alipay',
    'Myblog',
    'crispy_forms',

	'xadmin',
    'wechat_sdk',
    'requests',
	
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



WSGI_APPLICATION = 'mengup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'vevent',
        'USER': 'vevent',
        'PASSWORD': 'DFG^&*()sdhf@#nhD',
        'HOST': '221.236.172.241',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),

)



MEDIA_ROOT = '/photo/media'
TEMPLATE_DIRS = (
    os.path.join(HERE, 'templates').replace('\\', '/'),
)

MEDIA_ROOT = 'C:/Python27/Lib/site-packages/django/contrib/admin/media'

ADMIN_MEDIA_PREFIX = '/admin_media/'

