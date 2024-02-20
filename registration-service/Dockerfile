FROM --platform=linux/arm64/v8 python:3.10-slim-buster

WORKDIR /code

COPY ./app /code/app
COPY ./requirements.txt /code/requirements.txt
COPY .env /code
COPY ./migrations /code/migrations

RUN apt-get update && apt-get install -y libpq-dev \
    && apt-get clean
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# run flask
CMD ["python", "app/app.py"]
