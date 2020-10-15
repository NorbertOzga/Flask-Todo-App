from flask import jsonify

from . import bp


@bp.route('/task/all', methods=['GET'])
def task_all():
    return jsonify(['123', '345']), 200
