from sqlalchemy import Column, Integer, String

from app.infrastructure import db
from app.infrastructure.models.model_extension import ModelExtension


class People(db.Model, ModelExtension):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    role = Column(String)
