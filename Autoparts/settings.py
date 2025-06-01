"""
Configuración de Django para el proyecto Autoparts.

Generado por 'django-admin startproject' usando Django 3.0.5.

Para más información, consulta:
https://docs.djangoproject.com/en/3.0/topics/settings/

Para ver la lista completa de configuraciones:
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configuración rápida para desarrollo - no usar en producción
# https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


SECRET_KEY = '#!(x2a*5k*4$-wglppgl@lc!pdc)!@)&k+8$hd#)z)r5+-&tvf'


DEBUG = True

ALLOWED_HOSTS = []


# Definición de aplicaciones instaladas

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'parts',
    'accounts',
    'orders',
]

# Middleware (procesadores intermedios)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Autoparts.urls'

# Configuración de plantillas

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Autoparts.wsgi.application'


# Base de datos
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Validadores de contraseña
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


# Internacionalización
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Mexico_City'  # Puedes cambiarlo según tu país

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Archivos estáticos (CSS, JS, imágenes)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
STATICFILES_DIRS = [STATIC_DIR]

# Archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Etiquetas personalizadas para mensajes
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'alerta'
}
