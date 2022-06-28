## Budget App

A simple django web app used for budgeting your personal finance. 

### Technology stack
- Django
- Tailwind
- Alpine.js

## Environment variables
To run the web app locally, you need to create `.env` file in the project root
with the following environment variables:

```bash
# database environments
DB_NAME=budgetapp
DB_USER=user
DB_PASS=demo1234
DB_HOST=db-budgetapp

# webapp environments
SECRET_KEY=djangosecret
DJANGO_SETTINGS_MODULE=budgetapp.settings.development

```
Start the web app using docker compose

`docker compose up`

