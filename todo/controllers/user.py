import typing as tp

from sqlalchemy import exc
from marshmallow import ValidationError
from flask_bcrypt import generate_password_hash

from todo.extension import database
from todo.http_statuses import HttpStatus
from todo.models.user import User, user_schema


def get_user(user_id: int) -> tp.Tuple[tp.Dict, int]:
    data = User.query.get_or_404(user_id)

    return {"status": "success", "data": user_schema.dump(data)}, HttpStatus.OK


def create_user(json_data) -> tp.Tuple[tp.Dict, int]:
    if not json_data:
        return ({"status": "fail", "data": "No data is provided"},
                HttpStatus.BAD_REQUEST)
    try:
        data = user_schema.load(json_data)
    except ValidationError as e:
        return ({"status": "fail", "data": f"{e.messages}"},
                HttpStatus.UNPROCESSABLE_ENTITY)

    new_user = User(**data)
    new_user.password = generate_password_hash(new_user.password)
    database.session.add(new_user)

    try:
        database.session.commit()
    except exc.SQLAlchemyError as e:
        return ({"status": "fail", "message": e.code},
                HttpStatus.INTERNAL_SERVER_ERROR)

    return ({"status": "success", "data": user_schema.dump(new_user)},
            HttpStatus.CREATED)


def delete_user(user_id: int) -> tp.Tuple[tp.Dict, int]:
    user = User.query.filter(User.id == user_id)
    if user.count() == 0:
        return ({"status": "fail", "message": "User does not exists"},
                HttpStatus.BAD_REQUEST)

    user.delete()
    try:
        database.session.commit()
    except exc.SQLAlchemyError as e:
        return ({"status": "fail", "message": e.code},
                HttpStatus.INTERNAL_SERVER_ERROR)

    return {"status": "success", "data": None}, HttpStatus.OK
