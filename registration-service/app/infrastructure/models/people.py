from sqlalchemy import Column, Integer, String

from ..databases import db
from .model_extension import ModelExtension


class People(db.Model, ModelExtension):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    role = Column(String)
