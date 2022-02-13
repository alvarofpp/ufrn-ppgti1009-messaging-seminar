import sys

from core import RabbitClient


if __name__ == '__main__':
    client = RabbitClient()

    try:
        client.receive()
    except KeyboardInterrupt:
        client.close()
        sys.exit(0)
