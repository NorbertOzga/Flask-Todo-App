from flask import request, jsonify

from . import bp
from todo.controllers.user import login_user, create_user


@bp.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()

    body, status = login_user(json_data)

    return jsonify(body), status


@bp.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()

    body, status = create_user(json_data)

    return jsonify(body), status
