# -*- coding: utf-8 -*-

# Import standard library packages

# Import installed packages
from marshmallow import fields
# Import app code
from .base import BaseSchema


class UserSchema(BaseSchema):
    # Own properties
    email = fields.Email()
    first_name = fields.String()
    last_name = fields.String()
    is_active = fields.Boolean()
