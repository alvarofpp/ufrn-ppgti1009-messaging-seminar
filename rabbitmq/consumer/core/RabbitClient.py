import logging

from decouple import config
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel
from pika.credentials import PlainCredentials


class RabbitClient:
    def __init__(self):
        connection = self._get_connection()
        self.channel = self._get_channel(connection)

    def _get_connection(self) -> BlockingConnection:
        credentials = PlainCredentials(
            username=config('RABBITMQ_USER', 'guest'),
            password=config('RABBITMQ_PASSWORD', 'guest'),
        )

        parameters = ConnectionParameters(
            host=config('RABBITMQ_HOST', 'localhost'),
            port=config('RABBITMQ_PORT', 5672),
            credentials=credentials,
        )

        return BlockingConnection(parameters)

    def _get_channel(self, connection: BlockingConnection) -> BlockingChannel:
        channel = connection.channel()
        queue = config('RABBITMQ_QUEUE', 'default')

        channel.queue_declare(queue=queue)
        channel.basic_consume(
            queue=queue,
            on_message_callback=self.callback,
            auto_ack=True,
        )

        return channel

    def receive(self) -> None:
        logging.basicConfig(
            format='%(asctime)s | %(message)s',
            # encoding='utf-8',
            level=logging.INFO,
        )
        logging.info('Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def close(self) -> None:
        if self.channel is not None:
            self.channel.close()
            logging.info('Channel closed!')

    @staticmethod
    def callback(channel, method, properties, body):
        message = body.decode('utf-8')
        logging.info('Received: "{}"'.format(message))
