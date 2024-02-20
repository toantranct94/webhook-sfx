FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app
COPY .env /code

RUN pip install --no-cache-dir -r requirements.txt
ENV ENV=dev

CMD celery -A app.workers.consumer worker --loglevel=info
