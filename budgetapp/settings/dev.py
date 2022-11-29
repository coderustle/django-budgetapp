"""
Django settings for budgetapp project.
"""

# pylint: disable=wildcard-import unused-wildcard-import

import warnings

from .base import *

# Get rid of whitenoise "No directory at" warning, as it's not helpful when running tests.

# Related:
#   - https://github.com/evansd/whitenoise/issues/215
#   - https://github.com/evansd/whitenoise/issues/191
#   - https://github.com/evansd/whitenoise/commit/4204494d44213f7a51229de8bc224cf6d84c01eb
warnings.filterwarnings(
    "ignore", message="No directory at", module="whitenoise.base"
)

# GENERAL
# -----------------------------------------------------------------------------
DEBUG = True

# DATABASES
# -----------------------------------------------------------------------------
# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASS"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": "5432",
    }
}

# TEMPLATES
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "budgetapp/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "debug": True,
        },
    },
]

# For tests to speed up
# -----------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
