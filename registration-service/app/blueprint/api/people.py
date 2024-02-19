""" This module contains the 'webhook' Blueprint which organize and
group, views related to the index endpoint of HTTP REST API.
"""


from app.dependency_container import DependencyContainer
from app.infrastructure import PeopleService
from dependency_injector.wiring import Provide, inject
from flask import Blueprint

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
    ]
):
    validated_data = CreatePeopleSchema().load(data)
    people_service.create_people(**validated_data)
    return create_message_response('People created', 201)


@bp.route('/<people_id>', methods=['PUT', 'PATCH'])
@body_required
@inject
def update_people(
    people_id: int,
    data: dict,
    people_service: PeopleService = Provide[
        DependencyContainer.people_service
    ]
):
    validated_data = UpdatePeopleSchema().load(data)
    people_service.update_people(people_id, **validated_data)
    return create_message_response('Updated people')


@bp.route('/<people_id>', methods=['DELETE'])
@inject
def delete_people(
    people_id: int,
    people_service: PeopleService = Provide[
        DependencyContainer.people_service
    ]
):
    people_service.delete_people(people_id)
    return create_message_response('Deleted people')
