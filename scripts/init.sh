#!/usr/bin/env bash
#
# Set Environments
set -e

# =========================================
# Get env vars in the Dockerfile to show up in the SSH session
# =========================================
eval $(printenv | sed -n "s/^\([^=]\+\)=\(.*\)$/export \1=\2/p" | sed 's/"/\\\"/g' | sed '/=/s//="/' | sed 's/$/"/' >> /etc/profile)

# =========================================
# Start SSH Server
# =========================================
service ssh start

# =========================================
# Litestream restore database
# =========================================
# Restore the database if it does not already exist.
if [ -f ./data/development.db ]; then
	echo "Database already exists, skipping restore"
else
	echo "No database found, restoring from replica if exists"
	litestream restore -v -if-replica-exists -o /opt/budgetapp/data/development.db "abs://budgetapp@databases/dev"
fi

# =========================================
# Start gunicorn process
# =========================================
exec litestream replicate -exec "gunicorn --bind=0.0.0.0 --timeout 600 --workers=4 --chdir /opt/budgetapp budgetapp.wsgi --access-logfile '-' --error-logfile '-'"
