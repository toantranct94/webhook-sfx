# tests/conftest.py
import os

import pytest
from dotenv import load_dotenv
from flask import Flask

from app import create_app

load_dotenv('./tests/test.env')


@pytest.fixture(scope='module')
def test_app():
    config = {
        'TESTING': True,
        'SERVER_NAME': '127.0.0.1:5000',
        'SQLALCHEMY_DATABASE_URI': os.getenv('DATABASE_URL'),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    }
    app = create_app(config)
    return app


@pytest.fixture(scope='module')
def test_client(test_app: Flask):
    with test_app.test_client() as client:
        with test_app.app_context():
            yield client
