from app.infrastructure import db

from app.infrastructure.models import WebhookConfig


class WebhookService:

    def get_subscriptions(self, event_type: str):
        subs = db.query(WebhookConfig.url).filter_by(
            event_type=event_type).all()
        return subs
