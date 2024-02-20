import os
from app.domain import EventType
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# Configure Celery to use RabbitMQ as the broker
app = Celery('tasks', broker=os.environ.get('CELERY_BROKER_URL'))


@app.task(bind=True, name=EventType.CREATED.value)
def process_created_event(_, data):
    print(f"Processing created event: {data}")


@app.task(bind=True, name=EventType.UPDATED.value)
def process_updated_event(_, data):
    print(f"Processing updated event: {data}")


@app.task(bind=True, name=EventType.DELETED.value)
def process_deleted_event(_, data):
    print(f"Processing deleted event: {data}")
