#!/usr/bin/env bash
#
# Set Environments
set -e

# =========================================
# Collect static files
# =========================================
python manage.py collectstatic --no-input

# =========================================
# Start gunicorn process
# =========================================
gunicorn --bind=0.0.0.0 --timeout 600 budgetapp.wsgi
