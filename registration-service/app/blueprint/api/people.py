""" This module contains the 'webhook' Blueprint which organize and
group, views related to the index endpoint of HTTP REST API.
"""


import logging

from dependency_injector.wiring import Provide, inject
from domain import EventType
from flask import Blueprint
from infrastructure import PeopleService, QueueService
from infrastructure.dependency_container import DependencyContainer

from ..middleware import body_required
from ..responses import create_message_response
from ..schemas import CreatePeopleSchema, UpdatePeopleSchema

bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route('/', methods=['POST'])
@body_required
@inject
def create_people(
    data: dict,
    people_service: PeopleService = Provide[
        DependencyContainer.people_service
    ],
    queue_service: QueueService = Provide[
        DependencyContainer.queue_service
    ]
):
    """
    Create a new people record.

    Args:
        data (dict): The data for creating the people record.
        people_service (PeopleService): The service for handling people-related
            operations.
        queue_service (QueueService): The service for handling queue-related
            operations.

    Returns:
        Response: The response object indicating the result of the operation.
    """
    validated_data = CreatePeopleSchema().load(data)
    people = people_service.create_people(**validated_data)
    queue_service.publish_message(people.to_dict(), EventType.CREATED.value)
    return create_message_response('People created', 201)


@bp.route('/<people_id>', methods=['PUT', 'PATCH'])
@body_required
@inject
def update_people(
    people_id: int,
    data: dict,
    people_service: PeopleService = Provide[
        DependencyContainer.people_service
    ],
    queue_service: QueueService = Provide[
        DependencyContainer.queue_service
    ]
):
    """
    Update a people record.

    Args:
        people_id (int): The ID of the people record to update.
        data (dict): The data to update the people record with.
        people_service (PeopleService): The service for managing
            people records.
        queue_service (QueueService): The service for publishing messages
            to a queue.

    Returns:
        str: A message indicating that the people record has been updated.
    """
    validated_data = UpdatePeopleSchema().load(data)
    people = people_service.update_people(people_id, **validated_data)
    queue_service.publish_message(people.to_dict(), EventType.UPDATED.value)
    return create_message_response('Updated people')


@bp.route('/<people_id>', methods=['DELETE'])
@inject
def delete_people(
    people_id: int,
    people_service: PeopleService = Provide[
        DependencyContainer.people_service
    ],
    queue_service: QueueService = Provide[
        DependencyContainer.queue_service
    ]
):
    """
    Delete a person with the given ID.

    Args:
        people_id (int): The ID of the person to be deleted.
        people_service (PeopleService): The service used to delete the person.
        queue_service (QueueService): The service used to publish a message
            about the deletion.

    Returns:
        str: A message indicating that the person has been deleted.
    """
    people = people_service.delete_people(people_id)
    queue_service.publish_message(people.to_dict(), EventType.DELETED.value)
    return create_message_response('Deleted people')


@bp.route('/callback', methods=['POST'])
@body_required
@inject
def callback(
    data: dict,
):
    """
    Handle the callback endpoint.

    Args:
        data (dict): The data received in the callback.

    Returns:
        Response: The response indicating the callback was received.
    """
    logging.info(f"Received callback: {data}")
    return create_message_response('Received', 200)
