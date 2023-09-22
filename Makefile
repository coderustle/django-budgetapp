ifneq (,$(wildcard ./.env))
    include .env
    export
endif

#--------------------------------------------------------
# Docker commands
#--------------------------------------------------------
build-dev:
	docker build . --target development \
	--build-arg SECRET_KEY=$(SECRET_KEY) \
	--build-arg DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS_MODULE) \
	--build-arg PYTHON_REQUIREMENTS_FILE=test \
	--no-cache \
	--tag budgetapp:dev

run-dev:
	docker run --name budgetapp -it --rm \
	-p 8000:8000 budgetapp:dev bash

#--------------------------------------------------------
# Run unit tests
#--------------------------------------------------------
test:
	python manage.py test --exclude-tag=integration \
	-v 0 --failfast

#--------------------------------------------------------
# Run integration tests
#--------------------------------------------------------
test-integration:
	python manage.py test \
	tests.integration -v 0 --failfast
