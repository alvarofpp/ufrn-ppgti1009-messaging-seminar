# RabbitMQ "Hello World"

First you need to build the Docker images:

```shell
make build
```

After that, you should run `kafka` and `zookeeper`:

```shell
make up
# or
make up-silent
```

Now you need to create a topic:

```shell
make create-topic name=hello partitions=1
```

In another terminal, you must up `kafka-consumer`:

```shell
make up-consumer
```

In another terminal, you can test Kafka:

```shell
make send
```

---

## Others commands

Run the consumer through Kafka:

```shell
make create-consumer topic=hello
```

Run the producer through Kafka:

```shell
make create-producer topic=hello
```
