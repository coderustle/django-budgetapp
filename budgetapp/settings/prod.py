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
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "data/production.db",
    }
}
