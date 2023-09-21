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
# Unit test commands
#--------------------------------------------------------
test:
	python manage.py test \
	tests.unit -v 0 --failfast --keepdb

test-users:
	python manage.py test \
	tests.unit.users -v 0 --failfast --keepdb

#--------------------------------------------------------
# Functional test commands
#--------------------------------------------------------
test-integration:
	python manage.py test \
	tests.integration -v 0 --failfast --keepdb
