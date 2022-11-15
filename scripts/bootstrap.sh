#!/usr/bin/env bash
#
# Set Environments
set -e

if [ ! -f ".env" ]; then
    
    # Create the .env file
    touch .env
    
    echo 'BUILD_ENV="local"' >>.env
    echo " " >>.env
    echo "# Django variables"  >>.env
    echo "SECRET_KEY=\"$(cat /dev/urandom | tr -dc '[:alpha:]' | fold -w ${1:-50} | head -n 1)\"" >>.env
    
    echo 'DJANGO_SETTINGS_MODULE="budgetapp.settings.dev"' >>.env
    echo 'DJANGO_DEBUG="True"' >>.env
    
    echo " " >>.env
    echo "# Database variables"  >>.env
    echo 'DB_NAME="budgetapp_dev"' >>.env
    echo 'DB_HOST="db-budgetapp"' >>.env
    echo 'DB_PASS="abc123"' >>.env
    echo 'DB_USER="budget"' >>.env
    echo " " >>.env
    
fi

# =========================================
# Install node packages
# =========================================
yarn install

# =========================================
# Build docker images
# =========================================
docker compose up
