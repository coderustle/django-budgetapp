## Budget App

This is a django web app for personal finance budgeting.

### Technology stack

- Htmx
- Django
- Alpine.js
- Tailwindcss

### Run locally

1. Run bootstrap.sh script: `./scripts/bootstrap.sh`
2. Start Django: `python manage.py runserver`

If you want to run the app in docker container run the following command:

```bash

docker compose --profile webapp build
docker compose --profile webapp up

```

Make sure you update the `DB_HOST` and replace `localhost` with `db` service.

### Run tests

Run unit tests
`python manage.py test -v 0 --failfast tests.unit`

Run functional tests
`python manage.py test -v 0 --failfast tests.functional`

### Webpack libaries and plugins

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
