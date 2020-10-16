from marshmallow import fields

from todo import database, marshmallow


class Task(database.Model):
    __tablename__ = 'tasks'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer,
                              database.ForeignKey(
                                  'users.id',
                                  ondelete='CASCADE'
                              ),
                              nullable=False)
    title = database.Column(database.String, nullable=False)
    description = database.Column(database.String, nullable=True)
    add_time = database.Column(database.DateTime, nullable=False)


class TaskSchema(marshmallow.Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer()
    title = fields.String()
    description = fields.String()
    add_time = fields.DateTime()


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
