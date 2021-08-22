.PHONY: help
help:
	@echo "--------------- Merlin ---------------"
	@echo "make help                 -Display this list"
	@echo "make build                -Build docker container for local use"
	@echo "make migrate              -Run Django migrations"
	@echo "make makemigrations app={app_name}  -create migrations for an app"
	@echo "make app name={app_name} -Creates a new django app" 

.PHONY: build
build: 
	docker-compose build

.PHONY: app
app:
	docker-compose run --rm web python manage.py startapp $(name)

.PHONY: makemigrations
makemigrations:
	docker-compose run --rm web python manage.py makemigrations $(app)

.PHONY: migrate
migrate:
	docker-compose run --rm web python manage.py migrate