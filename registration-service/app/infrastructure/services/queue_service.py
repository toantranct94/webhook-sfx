import json
import logging
import os
import time
import uuid

import pika
from infrastructure.singleton import singleton

logging.basicConfig(level=logging.INFO)


@singleton
class QueueService():
    """
    A class representing a queue service for publishing messages to RabbitMQ.

    Attributes:
        connection: The connection to RabbitMQ.
        channel: The channel for communication with RabbitMQ.

    Methods:
        __init__: Initializes the QueueService object.
        publish_message: Publishes a message to RabbitMQ.
        close: Closes the connection to RabbitMQ.
    """

    def __init__(
        self,
        host: str = os.getenv('QUEUE_HOST', 'localhost'),
        retry_attempts: int = 5,
        retry_delay: int = 2,
    ):
        """
        Initializes the QueueService object.

        Parameters:
            host (str): The host of the RabbitMQ server.
                Defaults to 'localhost'.
            retry_attempts (int): The number of retry attempts to
                establish a connection. Defaults to 5.
            retry_delay (int): The delay in seconds between retry attempts.
                Defaults to 2.
        """
        for attempt in range(retry_attempts):
            try:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host=host))
                logging.info("Connected to RabbitMQ")
                break
            except Exception:
                logging.error(
                    (f"Connection attempt {attempt + 1} failed."
                        f"Retrying in {retry_delay} seconds..."))
                time.sleep(retry_delay)

        self.channel = self.connection.channel()

    def publish_message(
        self,
        message: dict,
        event_type: str,
        routing_key: str = 'celery'
    ):
        """
        Publishes a message to RabbitMQ.

        Parameters:
            message (dict): The message to be published.
            event_type (str): The type of the event.
            routing_key (str): The routing key for the message.
                Defaults to 'celery'.
        """
        properties = pika.BasicProperties(
            content_type='application/json',
            delivery_mode=1,)

        body = {
            'task': event_type,
            'id': uuid.uuid4().hex,
            'args': [],
            'kwargs': {
                'event_type': event_type,
                'message': message,
            },
        }

        self.channel.basic_publish(
            exchange='',
            routing_key=routing_key,
            body=json.dumps(body),
            properties=properties)

        logging.info("Message published")

    def close(self):
        """
        Closes the connection to RabbitMQ.
        """
        self.connection.close()
        logging.info("Disconnected from RabbitMQ")
