"""
WSGI config for budgetapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ENV_FILE = Path(__file__).resolve().parent.parent / ".env"

dotenv.load_dotenv(ENV_FILE)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "budgetapp.settings.dev")

application = get_wsgi_application()
