
#--------------------------------------------------------
# Unit test commands
#--------------------------------------------------------
test:
	python manage.py test \
	tests.unit -v 0 --failfast --keepdb

test-users:
	python manage.py test \
	tests.unit.users -v 0 --failfast --keepdb
