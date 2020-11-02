import typing as tp

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import exc

from todo.extension import database
from todo.http_statuses import HttpStatus
from todo.models.user import User, user_schema


def signup(email: str, name: str, password: str) -> tp.Tuple[tp.Dict, int]:
    user = User.query.filter_by(User.email == email).first()

    if user:
        return ({"status": "fail", "message": "User already exists"},
                HttpStatus.BAD_REQUEST)

    new_user = User(name=name,
                    email=email,
                    password=generate_password_hash(password, method='sha256'))

    database.session.add(new_user)
    try:
        database.session.commit()
    except exc.SQLAlchemyError as e:
        return ({"status": "fail", "message": e},
                HttpStatus.INTERNAL_SERVER_ERROR)

    return ({"status": "success", "data": user_schema.dump(new_user)},
            HttpStatus.OK)


def login():
    raise NotImplemented()
