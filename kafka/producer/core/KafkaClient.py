from json import dumps
import logging
from typing import Dict, Union

from decouple import config
from kafka import KafkaProducer


class KafkaClient:
    def __init__(self):
        self.producer = None
        self.topic = None

    def _get_server(self) -> str:
        host = config('KAFKA_HOST', 'localhost')
        port = config('KAFKA_PORT', '9092')

        return '{}:{}'.format(host, port)

    @staticmethod
    def value_serializer(value) -> bytes:
        return dumps(value).encode('utf-8')

    def init(self) -> None:
        self.topic = config('KAFKA_TOPIC', 'default')
        self.producer = KafkaProducer(
            value_serializer=self.value_serializer,
            bootstrap_servers=self._get_server(),
        )

    def close(self) -> None:
        if self.producer is not None:
            self.producer.close()
            logging.info('Connection closed!')

    def send(self, data: Union[str, Dict]) -> None:
        if isinstance(data, str):
            data = {'value': data}

        self.producer.send(self.topic, value=data)
        self.producer.flush()
