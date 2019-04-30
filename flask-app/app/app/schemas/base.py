# -*- coding: utf-8 -*-

# Import installed packages
from marshmallow import fields
from marshmallow import Schema


class BaseSchema(Schema):
    def __init__(self, strict=True, **kwargs):
        super(Schema, self).__init__(strict=strict, **kwargs)

    id = fields.Int()
    created_at = fields.DateTime()
