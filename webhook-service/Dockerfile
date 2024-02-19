FROM python:3.10-bullseye

EXPOSE 5000
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# run flask
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
