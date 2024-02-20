from marshmallow import Schema, fields


class WebhookConfigSchema(Schema):
    """
    Schema for validating webhook configuration.

    Attributes:
        url (str): The URL of the webhook.
        event_type (str): The type of event the webhook is triggered for.
        custom_headers (dict, optional): Custom headers to be included in
            the webhook request.
        custom_payload (dict, optional): Custom payload to be sent with
            the webhook request.
    """
    url = fields.Str(required=True)
    event_type = fields.Str(required=True)
    custom_headers = fields.Dict(required=False)
    custom_payload = fields.Dict(required=False)
