""" This module contains the 'webhook' Blueprint which organize and
group, views related to the index endpoint of HTTP REST API.
"""


from dependency_injector.wiring import Provide, inject
from flask import Blueprint
from infrastructure import WebhookService
from infrastructure.dependency_container import DependencyContainer

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
    """
    Upserts a subscription based on the provided data.

    Args:
        data (dict): The data containing the subscription details.
        webhook_service (WebhookService): The instance of the WebhookService class.

    Returns:
        Response: The response indicating the success of the operation.
    """
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
    """
    Delete a subscription for a given URL and event type.

    Args:
        url (str): The URL for the subscription.
        event_type (str): The event type for the subscription.
        webhook_service (WebhookService): The webhook service instance.

    Returns:
        Response: The response indicating the success of the deletion.
    """
    url = url.replace('~', '/')
    webhook_service.delete_subscription(url, event_type)
    return create_message_response('Subscription deleted', 200)
