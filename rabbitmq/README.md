# RabbitMQ "Hello World"

First you need to build the Docker images:

```shell
make build
```

After that, you can run the `rabbitmq` and `rabbitmq-consumer`:

```shell
make up
# or
make up-silent
```

In another terminal (if you used `make up`), you can test RabbitMQ:

```shell
make send
```
