from flask import request

from . import bp


@bp.route('/task', methods=['GET', 'POST'])
def task():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass


@bp.route('/task/<int:id>', methods=['GET', 'DELETE'])
def task_id():
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass


@bp.route('/task/all', methods=['GET'])
def task_all():
    pass
