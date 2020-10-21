from marshmallow import fields

from todo.extension import database, marshmallow
from todo.validators.common import cannot_be_empty


class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(50), nullable=False)
    password = database.Column(database.String(100), nullable=False)


class UserSchema(marshmallow.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(validate=[cannot_be_empty])
    email = fields.String(validate=[cannot_be_empty])
    password = fields.String(validate=[cannot_be_empty])


user_schema = UserSchema()
users_schema = UserSchema(many=True)
