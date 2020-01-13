# runs the whole project
.PHONY: start
start:
	docker-compose up --build --force-recreate -d

# stops the execution
.PHONY: stop
stop:
	docker-compose stop

# executes tests on the local machine
.PHONY: tests
tests:
	python -m unittest discover .