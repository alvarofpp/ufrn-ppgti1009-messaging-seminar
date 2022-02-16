from json import loads
import logging

from decouple import config
from kafka import KafkaConsumer


class KafkaClient:
    def __init__(self):
        self.consumer = None
        self.topic = None

    def _get_server(self) -> str:
        host = config('KAFKA_HOST', 'localhost')
        port = config('KAFKA_PORT', '9092')

        return '{}:{}'.format(host, port)

    @staticmethod
    def value_deserializer(value):
        value = value.decode('utf-8')
        logging.info('Received: {}'.format(value))
        return loads(value)

    def init(self) -> None:
        self.topic = config('KAFKA_TOPIC', 'default')
        self.consumer = KafkaConsumer(
            self.topic,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=config('KAFKA_GROUP', 'default-group'),
            value_deserializer=self.value_deserializer,
            bootstrap_servers=self._get_server(),
            api_version=(2, 5, 0),
        )

    def close(self) -> None:
        if self.consumer is not None:
            self.consumer.close()
            logging.info('Connection closed!')
