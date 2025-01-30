from config.settings.base import *

DEBUG = False

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True

ALLOWED_HOSTS = [HOST, f"{SUBDOMAIN}.{HOST}", f"www.{HOST}"]

CORS_ORIGIN_WHITELIST = [
    f"http://{HOST}",
    f"https://{HOST}",
    f"http://www.{HOST}",
    f"https://www.{HOST}",
]

CSRF_TRUSTED_ORIGINS = [
    f"http://{HOST}",
    f"https://{HOST}",
    f"http://{SUBDOMAIN}.{HOST}",
    f"https://{SUBDOMAIN}.{HOST}",
]
