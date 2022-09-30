"""
Django settings for budgetapp project.
"""

# pylint: disable=wildcard-import unused-wildcard-import

from .base import *

# GENERAL
# -----------------------------------------------------------------------------

DEBUG = True

ALLOWED_HOSTS = [
    "personalbudget.azurewebsites.net",
    "budget.madalintech.com",
    "localhost",
]

# SECURITY
# -----------------------------------------------------------------------------
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_TRUSTED_ORIGINS = ["https://personalbudget.azurewebsites.net"]

# DATABASES
# -----------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASS"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": "",
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}
