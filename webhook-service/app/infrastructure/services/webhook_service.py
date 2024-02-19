from app.infrastructure.databases import db
from ..models import WebhookConfig


class WebhookService:

    def get_subscriptions(self, event_type: str):
        subs = db.session.query(WebhookConfig).filter_by(
            event_type=event_type).all()
        return subs
