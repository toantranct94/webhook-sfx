from infrastructure.databases import db

from ..models import WebhookConfig


class WebhookService:
    """
    Service class for managing webhooks.
    """

    def upsert_subscription(self, config_data: dict):
        """
        Upserts a webhook subscription.

        Args:
            config_data (dict): The configuration data for the webhook.

        Returns:
            WebhookConfig: The updated or newly created webhook configuration.
        """
        webhook_config: WebhookConfig = WebhookConfig.query.filter_by(
            url=config_data['url'],
            event_type=config_data['event_type']
        ).first()

        if webhook_config:
            # Update fields as necessary
            webhook_config.custom_headers = config_data.get('custom_headers')
            webhook_config.custom_payload = config_data.get('custom_payload')
        else:
            webhook_config = WebhookConfig(**config_data)
            db.session.add(webhook_config)

        db.session.commit()

        return webhook_config

    def delete_subscription(self, url: str, event_type: str):
        """
        Deletes a webhook subscription.

        Args:
            url (str): The URL of the webhook.
            event_type (str): The event type of the webhook.

        Returns:
            None
        """
        db.session.query(WebhookConfig).filter(
            WebhookConfig.url == url,
            WebhookConfig.event_type == event_type
        ).delete()
        db.session.commit()
