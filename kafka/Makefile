# Variables
KAFKA_HOME=/opt/kafka
KAFKA_PORT=9092

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

.PHONY: up
up:
	@docker-compose up zookeeper kafka

.PHONY: up-silent
up-silent:
	@docker-compose up -d zookeeper kafka

.PHONY: send
send:
	@docker-compose run kafka-producer

.PHONY: logs
logs:
	@docker-compose logs --follow

.PHONY: create-topic
create-topic:
	@docker-compose exec kafka ${KAFKA_HOME}/bin/kafka-topics.sh --create --partitions ${partitions} --bootstrap-server localhost:${KAFKA_PORT} --topic ${name}

.PHONY: up-consumer
up-consumer:
	@docker-compose up kafka-consumer

.PHONY: create-consumer
create-consumer:
	@docker-compose exec kafka ${KAFKA_HOME}/bin/kafka-console-consumer.sh --from-beginning --bootstrap-server localhost:${KAFKA_PORT} --topic ${topic}

.PHONY: create-producer
create-producer:
	@docker-compose exec kafka ${KAFKA_HOME}/bin/kafka-console-producer.sh --broker-list localhost:${KAFKA_PORT} --topic ${topic}

.PHONY: scale
scale:
	@docker-compose scale kafka=${brokers}
