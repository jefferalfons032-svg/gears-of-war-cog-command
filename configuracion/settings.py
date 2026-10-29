
"""
Django settings for configuracion project.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración de seguridad
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-clave-solo-para-desarrollo"
)

DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Aplicaciones instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "gears_jeff",
]


# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Configuración principal
ROOT_URLCONF = "configuracion.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "configuracion.wsgi.application"


# Base de datos PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "gears_of_war"),
        "USER": os.environ.get("DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}


# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# Idioma y zona horaria
LANGUAGE_CODE = "es-co"

TIME_ZONE = "America/Bogota"

USE_I18N = True

USE_TZ = True


# Archivos estáticos
STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# Archivos multimedia
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# Tipo de clave primaria predeterminada
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
