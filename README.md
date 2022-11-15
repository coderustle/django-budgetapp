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
