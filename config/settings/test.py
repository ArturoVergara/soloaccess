from .base import *
from .base import env

DEBUG = False
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-rh3w890yi8bn8lkmv#d$%v_4-&adcukrpodm@ekm9%l7@1rrt9",
)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
