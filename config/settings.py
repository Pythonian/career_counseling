"""
Django settings for career compass project.
"""

from pathlib import Path

from decouple import Csv, config
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_bootstrap5",
    "crispy_forms",
    "career.apps.CareerConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": config("SQL_ENGINE"),
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT"),
    },
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "assets"

STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_TEMPLATES_PACK = "bootstrap5"

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

LOGOUT_REDIRECT_URL = "home"

DATA_UPLOAD_MAX_NUMBER_FIELDS = None

DEFAULT_FROM_EMAIL = config("DEFAULT_EMAIL")
EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_USE_TLS = True

if DEBUG:
    CORS_REPLACE_HTTPS_REFERER = False
    HOST_SCHEME = "http://"
    SECURE_FRAME_DENY = False
    SECURE_PROXY_SSL_HEADER = None
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_SECONDS = None
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
else:
    CORS_REPLACE_HTTPS_REFERER = True
    HOST_SCHEME = "https://"
    SECURE_FRAME_DENY = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 2592000
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REDIRECT_EXEMPT = []
