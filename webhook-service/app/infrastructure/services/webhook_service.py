from app.infrastructure import db
from app.infrastructure.models import WebhookConfig


class WebhookService:
    """
    Service class for managing webhooks.
    """

    def get_subscriptions(self, event_type: str):
        """
        Retrieves the subscriptions for a given event type.

        Args:
            event_type (str): The type of event.

        Returns:
            list: A list of subscription URLs.
        """
        subs = db.query(WebhookConfig.url).filter_by(
            event_type=event_type).all()
        return subs
