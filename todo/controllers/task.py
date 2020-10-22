import datetime
import typing as tp

from sqlalchemy import exc
from marshmallow import ValidationError

from todo.extension import database
from todo.http_statuses import HttpStatus
from todo.models.task import Task, task_schema, tasks_schema


def get_task(task_id: int) -> tp.Tuple[tp.Dict, int]:
    data = Task.query.get_or_404(task_id)

    return {"status": "success", "data": task_schema.dump(data)}, HttpStatus.OK


def get_active_tasks_for_user(user_id: int) -> tp.Tuple[tp.Dict, int]:
    tasks = Task.query.filter(Task.user_id == user_id, Task.active is True)
    if tasks.count() == 0:
        return ({"status": "success", "data": None},
                HttpStatus.BAD_REQUEST)

    return ({"status": "success", "data": tasks_schema.dump(tasks)},
            HttpStatus.OK)


def get_all_tasks_for_user(user_id: int) -> tp.Tuple[tp.Dict, int]:
    tasks = Task.query.filter(Task.user_id == user_id)
    if tasks.count() == 0:
        return ({"status": "success", "data": None},
                HttpStatus.BAD_REQUEST)

    return ({"status": "success", "data": task_schema.dump(tasks)},
            HttpStatus.OK)


def add_task(json_data) -> tp.Tuple[tp.Dict, int]:
    if not json_data:
        return ({"status": "fail", "data": "No data is provided"},
                HttpStatus.BAD_REQUEST)

    try:
        data = task_schema.load(json_data)
    except ValidationError as e:
        return ({"status": "fail", "data": f"{e.messages}"},
                HttpStatus.UNPROCESSABLE_ENTITY)

    new_task = Task(**data)
    new_task.add_time = datetime.datetime.now()
    database.session.add(new_task)

    try:
        database.session.commit()
    except exc.SQLAlchemyError as e:
        return ({"status": "fail", "message": e},
                HttpStatus.INTERNAL_SERVER_ERROR)

    return ({"status": "success", "data": task_schema.dump(new_task)},
            HttpStatus.CREATED)


def delete_task(task_id: int) -> tp.Tuple[tp.Dict, int]:
    task = Task.query.filter(Task.id == task_id)
    if task.count() == 0:
        return ({"status": "fail", "message": "Task does not exist"},
                HttpStatus.BAD_REQUEST)

    task.delete()
    try:
        database.session.commit()
    except exc.SQLAlchemyError as e:
        return ({"status": "fail", "message": e.code},
                HttpStatus.INTERNAL_SERVER_ERROR)

    return {"status": "success", "data": None}, HttpStatus.OK


def update_task(task_id: int, json_data) -> tp.Tuple[tp.Dict, int]:
    raise NotImplemented()
