# Budget App

This is a django web app for personal finance budgeting.

[![Build](https://github.com/madalinpopa/budgetapp/actions/workflows/main.yml/badge.svg?branch=dev)](https://github.com/madalinpopa/budgetapp/actions/workflows/main.yml)

## Technology stack

- Htmx
- Django
- Alpine.js
- Tailwindcss
- Litestream

## Run locally

1. Create a virtual environment: `python3.11 -m venv .venv && source .venv/bin/activate`
2. Install requirements: `pip install -r requirements/local.txt`
3. Run bootstrap.sh script: `./scripts/bootstrap.py`
4. Run database migrations: `python manage.py migrate`
5. Start litestream and Node: `docker compose up -d`
6. Start Django: `python manage.py runserver`

**Note:** For litestream you need to update the `REPLICA_URL` in `docker-compose.yml` to point to a local file path.

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
REPLICA_URL                  # The place where litestream to replicate db
LITESTREAM_AZURE_ACCOUNT_KEY # Azure account key used by litestream
```

## Contributing

1. Open an issue and describe the changes that you want to do.
2. Fork the repository
3. Create a a new branch to work on changes that you want to add.
4. Push the new branch to GitHub, open a pull request and mention the issue from step 1. Enjoy!

Be kind and polite with others, don't forget we are doing this for fun and because we like to code.
