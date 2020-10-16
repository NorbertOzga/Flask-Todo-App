from marshmallow import ValidationError


max_priority = 10
min_priority = 1


def is_in_allowed_priority_range(priority: int):
    if max_priority > priority < min_priority:
        raise ValidationError('Priority is not in allowed range')