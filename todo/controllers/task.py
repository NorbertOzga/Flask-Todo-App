import typing as tp

from sqlalchemy import exc
from marshmallow import ValidationError

from todo.extension import database
from todo.http_statuses import HttpStatus
from todo.models.task import Task, task_schema


def get_task(task_id: int) -> tp.Tuple[tp.Dict, int]:
    data = Task.query.get_or_404(task_id)
    return {"status": "success", "data": task_schema.dump(data)}, HttpStatus.OK


def get_active_tasks_for_user(user_id: int) -> tp.Tuple[tp.Dict, int]:
    raise NotImplemented()


def get_all_tasks_for_user(user_id: int) -> tp.Tuple[tp.Dict, int]:
    raise NotImplemented()


def add_task(json_data) -> tp.Tuple[tp.Dict, int]:
    raise NotImplemented()


def delete_task(task_id: int) -> tp.Tuple[tp.Dict, int]:
    raise NotImplemented()


def update_task(task_id: int) -> tp.Tuple[tp.Dict, int]:
    raise NotImplemented()