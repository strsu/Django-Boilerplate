from config.settings.base import *

DEBUG = False

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

ALLOWED_HOSTS = [
    f"{SUBDOMAIN}.{HOST}",
]

CORS_ORIGIN_WHITELIST = [
    f"http://dev.{HOST}",
    f"https://dev.{HOST}",
]

CSRF_TRUSTED_ORIGINS = [
    f"http://{SUBDOMAIN}.{HOST}",
    f"https://{SUBDOMAIN}.{HOST}",
]
