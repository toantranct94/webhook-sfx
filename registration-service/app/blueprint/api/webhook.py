""" This module contains the 'webhook' Blueprint which organize and
group, views related to the index endpoint of HTTP REST API.
"""


from app.dependency_container import DependencyContainer
from app.infrastructure import WebhookService
from dependency_injector.wiring import Provide, inject
from flask import Blueprint

from ..middleware import body_required
from ..responses import create_message_response
from ..schemas import WebhookConfigSchema

bp = Blueprint('webhook', __name__, url_prefix='/subscriptions')


@bp.route('/', methods=['POST'])
@body_required
@inject
def upsert_subscription(
    data: dict,
    webhook_service: WebhookService = Provide[
        DependencyContainer.webhook_service
    ]
):
    validated_data = WebhookConfigSchema().load(data)
    webhook_service.upsert_subscription(validated_data)
    return create_message_response('Subscription created', 201)


@bp.route('/<path:url>/<event_type>', methods=['DELETE'])
@inject
def delete_subscription(
    url: str,
    event_type: str,
    webhook_service: WebhookService = Provide[
        DependencyContainer.webhook_service
    ]
):
    url = url.replace('~', '/')
    webhook_service.delete_subscription(url, event_type)
    return create_message_response('Subscription deleted', 200)
