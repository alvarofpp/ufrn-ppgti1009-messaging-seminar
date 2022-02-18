# RabbitMQ "Hello World"

First you need to build the Docker images:

```shell
make build
```

After that, you can run the `rabbitmq` and `rabbitmq-consumer`:

```shell
docker-compose up rabbitmq
```

In another terminal:

```shell
docker-compose up rabbitmq-consumer
```

In another terminal you can test RabbitMQ:

```shell
make send
```
