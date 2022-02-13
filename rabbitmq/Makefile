# Variables
DOCKER_IMAGE_LINTER=alvarofpp/python-linter
ROOT=$(shell pwd)
LINT_COMMIT_TARGET_BRANCH=origin/main

# Commands
.PHONY: build
build:
	@docker-compose build

.PHONY: build-no-cache
build-no-cache:
	@docker-compose build --no-cache

.PHONY:
down:
	@docker-compose down

.PHONY:
send:
	@docker-compose run rabbitmq-producer

.PHONY:
up:
	@docker-compose up rabbitmq rabbitmq-consumer

.PHONY:
up-silent:
	@docker-compose up -d rabbitmq rabbitmq-consumer

.PHONY: logs
logs:
	@docker-compose logs --follow