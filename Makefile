
#--------------------------------------------------------
# Unit test commands
#--------------------------------------------------------
test-unit:
	python manage.py test \
	tests.unit -v 0 --failfast --keepdb

test-unit-users:
	python manage.py test \
	tests.unit.users -v 0 --failfast --keepdb

#--------------------------------------------------------
# Functional test commands
#--------------------------------------------------------
test-functional:
	python manage.py test \
	tests.functional -v 0 --failfast --keepdb

test-functional-users:
	python manage.py test \
	tests.functional.users -v 0 --failfast --keepdb
