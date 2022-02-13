import sys

from core import RabbitClient


if __name__ == '__main__':
    client = RabbitClient()

    try:
        while True:
            message = input('Send a message: ')
            client.send(message)
    except KeyboardInterrupt:
        client.close()
        sys.exit(0)
