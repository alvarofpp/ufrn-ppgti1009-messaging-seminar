import logging
import sys
from time import sleep

from core import KafkaClient
from kafka.errors import NoBrokersAvailable

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s | %(message)s',
        level=logging.INFO,
    )
    connection_attempt = 0
    client = KafkaClient()

    while connection_attempt < 3:
        try:
            client.init()
            while True:
                message = input('Send a message: ')
                client.send(message)
        except NoBrokersAvailable:
            connection_attempt += 1
            attempt_text = '(attempt {})'.format(connection_attempt)
            logging.warning('Connection attempt to Kafka failed {}'.format(attempt_text))
            logging.info('A new attempt will take place soon')
            sleep(5)
        except KeyboardInterrupt:
            client.close()
            sys.exit(0)
