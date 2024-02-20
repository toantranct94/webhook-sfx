"""This module provides means to perform operations on the database
using the SQLAlchemy library."""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker

if os.getenv('ENV') == 'dev':
    load_dotenv()
else:
    load_dotenv('.env.local', override=True)


database_url = os.getenv('DATABASE_URL')
engine = create_engine(database_url, convert_unicode=True)

# Create a scoped session factory
db = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db.query_property()
