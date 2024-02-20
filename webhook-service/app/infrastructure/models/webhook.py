from app.infrastructure.databases import Base
from app.infrastructure.models.model_extension import ModelExtension
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB


class WebhookConfig(Base, ModelExtension):
    __tablename__ = 'webhook_config'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    event_type = Column(String, nullable=False)
    custom_headers = Column(JSONB)
    custom_payload = Column(JSONB)

    __table_args__ = (
        UniqueConstraint('url', 'event_type', name='uix_url_event_type'),
    )
