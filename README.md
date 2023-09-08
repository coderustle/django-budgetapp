# Budget App

This is a django web app for personal finance budgeting.

[![Build](https://github.com/madalinpopa/budgetapp/actions/workflows/main.yml/badge.svg?branch=dev)](https://github.com/madalinpopa/budgetapp/actions/workflows/main.yml)

## Technology stack

- Htmx
- Django
- Alpine.js
- Tailwindcss

## Run locally

1. Create a virtual environment: `python3.11 -m venv .venv && source .venv/bin/activate`
2. Install requirements: `pip install -r requirements/local.txt`
3. Run bootstrap.sh script: `./scripts/bootstrap.py`
4. Start database and Node: `docker compose up -d`
5. Run database migrations: `python manage.py migrate`
6. Start Django: `python manage.py runserver`

If you want to run the app in docker container run the following command:

```bash

docker compose --profile webapp build
docker compose --profile webapp up

```

If you run the app in container, make sure you update the `DB_HOST` and replace `localhost` with `db` service.

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
BUILD_ENV                   # requirements.txt file name to build in docker stage
SECRET_KEY                  # django secret key

# Database
DB_NAME                     # postgres database name
DB_USER                     # postgres datbase user
DB_PASS                     # postgres database pass
DB_HOST                     # postgres host
DB_PORT                     # postgres port
```

## Contributing

1. Open an issue and describe the changes that you want to do.
2. Fork the repository
3. Create a a new branch to work on changes that you want to add.
4. Push the new branch to GitHub, open a pull request and mention the issue from step 1. Enjoy!

Be kind and polite with others, don't forget we are doing this for fun and because we like to code.
