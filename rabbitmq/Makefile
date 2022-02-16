# Commands
.PHONY: build
build:
	@docker-compose build

.PHONY: build-no-cache
build-no-cache:
	@docker-compose build --no-cache

.PHONY: down
down:
	@docker-compose down

.PHONY: send
send:
	@docker-compose run rabbitmq-producer

.PHONY: up
up:
	@docker-compose up rabbitmq rabbitmq-consumer

.PHONY: up-silent
up-silent:
	@docker-compose up -d rabbitmq rabbitmq-consumer

.PHONY: logs
logs:
	@docker-compose logs --follow