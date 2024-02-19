from marshmallow import Schema, fields


class CreatePeopleSchema(Schema):
    email = fields.Email(required=True)
    role = fields.Str(required=True)


class UpdatePeopleSchema(Schema):
    role = fields.Str(required=True)


class PeopleSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Email(required=True)
    role = fields.Str(required=True)
