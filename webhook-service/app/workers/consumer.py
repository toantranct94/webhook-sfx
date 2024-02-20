import logging
import os
from typing import Any

from app.clients import APIClient
from app.domain import EventType
from app.infrastructure import WebhookService
from celery import Celery
from .tasks import BaseTaskWithRetry

logging.basicConfig(level=logging.INFO)

app = Celery('tasks', broker=os.environ.get('CELERY_BROKER_URL'))

client = APIClient()
webhook_service = WebhookService()


@app.task(bind=True, name=EventType.CREATED.value, base=BaseTaskWithRetry)
def process_created_event(self, event_type: str, message: Any):
    process_event(event_type, message)


@app.task(bind=True, name=EventType.UPDATED.value, base=BaseTaskWithRetry)
def process_updated_event(self, event_type: str, message: Any):
    process_event(event_type, message)



@app.task(bind=True, name=EventType.DELETED.value, base=BaseTaskWithRetry)
def process_deleted_event(self, event_type: str, message: Any):
    process_event(event_type, message)


def process_event(event_type: str, message: Any):
    logging.info(f"Processing {event_type} event: {message}")
    urls = get_endpoint(event_type)
    for url in urls:
        process_http_request(url[0], message)


def get_endpoint(event_type: str) -> str:
    urls = webhook_service.get_subscriptions(event_type)
    return urls


def process_http_request(url: str, message: Any):
    client.forward_event(url, message)
