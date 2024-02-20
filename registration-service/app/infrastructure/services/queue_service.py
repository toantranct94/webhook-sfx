import json
import logging
import os
import time
import uuid

import pika
from app.singleton import singleton

logging.basicConfig(level=logging.INFO)


@singleton
class QueueService():

    def __init__(
        self,
        host: str = os.getenv('QUEUE_HOST', 'localhost'),
        retry_attempts: int = 5,
        retry_delay: int = 2,
    ):
        print("QueueService __init__", host)
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
        properties = pika.BasicProperties(
            content_type='application/json',
            delivery_mode=1,)

        body = {
            'task': event_type,
            'id': uuid.uuid4().hex,
            'args': [message],
            'kwargs': {},
        }

        self.channel.basic_publish(
            exchange='',
            routing_key=routing_key,
            body=json.dumps(body),
            properties=properties)

        logging.info("Message published")

    def close(self):
        self.connection.close()
        logging.info("Disconnected from RabbitMQ")
