from marshmallow import ValidationError


def cannot_be_empty(data):
    if not data:
        raise ValidationError("Data is not provided")
