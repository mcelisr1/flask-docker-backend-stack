# -*- coding: utf-8 -*-

# Import installed packages
from marshmallow import fields
# Import app code
from .base import BaseSchema


class RoleSchema(BaseSchema):
    # Own properties
    code = fields.String()
    name = fields.String()
    description = fields.String()
