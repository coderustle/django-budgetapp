# Budget App

[![Build](https://github.com/coderustle/django-budgetapp/actions/workflows/dev.yml/badge.svg?branch=dev)](https://github.com/coderustle/django-budgetapp/actions/workflows/dev.yml)

Budget App is a tool designed to help you manage your money. Built on the Django platform, it offers an easy way to keep track of your finances. The clean design, thanks to Tailwindcss, ensures a user-friendly experience.

## Technology stack

**Django**
Django is the primary web framework that powers the app, making it easier to build web applications quickly and with less code.

**Htmx**
Htmx allows parts of web pages to be updated seamlessly without a full page reload, providing a smooth and dynamic user

**Alpine.js**
A minimal framework for composing JavaScript-rich components, Alpine.js offers functionality similar to Vue but with a smaller footprint. It helps create dynamic components within the app.

**Tailwindcss**
This utility-first CSS framework aids in creating custom, responsive designs quickly, giving the app its modern and sleek appearance.

**Litestream**
Used for database replication, ensuring data integrity and availability. It also provides integration with storage platforms like Azure.

**Webpack**
 A module bundler, Webpack is used to package and optimize JavaScript and CSS assets for the app.

## Run locally

1. Create a virtual environment: `python3.11 -m venv .venv && source .venv/bin/activate`
2. Install requirements: `pip install -r requirements/local.txt`
3. Run bootstrap.sh script: `./scripts/bootstrap.py`
4. Run database migrations: `python manage.py migrate`
5. Generate static files: `yarn run build:prod`
6. Start Django: `python manage.py runserver`

If you want to build and auto-reload static files run `docker compose up -d`

## Run tests

Run unit tests
`python manage.py test -v 0 --failfast tests.unit`

Run functional tests
`python manage.py test -v 0 --failfast tests.functional`

## Webpack libaries and plugins

```bash

# Webpack
webpack                        # Webpack
webpack-cli                    # Webpack cli
webpack-merge                  # Used to combine multiple webpack configuration
webpack-bundle-tracker         # Used to track webpack bundle

# Webpack plugins
mini-css-extract-plugin        # Used to extract css into separate file
compression-webpack-plugin     # Used to compress the js files

# Webpack loaders
css-loader                     # Used to load css
postcss-loader                 # Used with tailwindcss to parse css
babel-loader                   # Used to load js

# Other libraries
@babel/core                    # Javascript compiler
@babel/preset-env              # Javascript compiler
htmx.org                       # Htmx gives you access to AJAX, CSS Transitions, WebSockets and Server Sent Events
alpinejs                       # Create Vue like components
autoprefixer                   # PostCSS plugin to parse CSS and add vendor prefixes to CSS rules
postcss                        # A tool for transforming CSS with JavaScript
tailwindcss                    # A utility-first CSS framework for rapid UI development

```

## Environment variables explained

```bash
# Django
DJANGO_SETTINGS_MODULE      # django settings module
PYTHON_REQUIREMENTS_FILE    # requirements.txt file name to build in docker
SECRET_KEY                  # django secret key

# LiteStream
REPLICA_URL                  # (Optional) Replica db url path (Azure, S3)
LITESTREAM_AZURE_ACCOUNT_KEY # (Optional) Azure storage account key
DEV_DB_PATH                  # Path to dev database
PROD_DB_PATH                 # Path to prod database
```

## Contributing

1. Open an issue and describe the changes that you want to do.
2. Fork the repository
3. Create a a new branch to work on changes that you want to add.
4. Push the new branch to GitHub, open a pull request and mention the issue from step 1. Enjoy!

Be kind and polite with others, don't forget we are doing this for fun and because we like to code.
