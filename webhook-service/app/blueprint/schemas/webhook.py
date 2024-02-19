from marshmallow import Schema, fields


class WebhookConfigSchema(Schema):
    url = fields.Str(required=True)
    event_type = fields.Str(required=True)
    custom_headers = fields.Dict(required=False)
    custom_payload = fields.Dict(required=False)
