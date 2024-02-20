from marshmallow import Schema, fields


class CreatePeopleSchema(Schema):
    """
    Schema for creating a new person.

    Attributes:
        email (str): The email of the person. Required.
        role (str): The role of the person. Required.
    """
    email = fields.Email(required=True)
    role = fields.Str(required=True)


class UpdatePeopleSchema(Schema):
    """
    Schema for updating people information.
    """
    role = fields.Str(required=True)


class PeopleSchema(Schema):
    """
    Schema for representing people.
    """
    id = fields.Int(required=True)
    email = fields.Email(required=True)
    role = fields.Str(required=True)
