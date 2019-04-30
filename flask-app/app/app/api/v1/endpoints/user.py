# -*- coding: utf-8 -*-

# Import installed packages
from flask import abort
from flask_apispec import doc, use_kwargs, marshal_with
from flask_jwt_extended import jwt_required
from webargs import fields

# Import app code
from app.api.v1.api_docs import docs
from app.api.v1.utils.general import datetime_now
from app.core import data
from app.core.db.session import db_session
from app.core.security import pwd_context
from app.main import app

# Import providers
from app.providers import user_provider

# Import required schemas
from app.schemas.msg import MsgSchema
from app.schemas.user import UserSchema

# Import required models
from app.models.user import User


@docs.register
@doc(
    description='Create a new user in the system.',
    tags=['users'])
@app.route(
    f'{data.V1_STR}/users',
    methods=['POST']
)
@use_kwargs({
    'email': fields.Email(required=True),
    'password': fields.String(required=True)
})
@marshal_with(UserSchema())
def route_users_post(
    email=None,
    password=None
):
    user_obj = user_provider.get_by_email(email=email)
    if user_obj is not None:
        abort(400, 'The email to register already exists in the system.')

    new_user_obj = User(
        created_at=datetime_now(),
        email=email,
        password=pwd_context.hash(password)
    )
    db_session.add(new_user_obj)
    db_session.commit()

    return new_user_obj


@docs.register
@doc(
    description='Read existing users in the system.',
    tags=['users'])
@app.route(
    f'{data.V1_STR}/users',
    methods=['GET']
)
@marshal_with(UserSchema(many=True))
def route_users_get():
    return user_provider.get_all()


@docs.register
@doc(
    description='{} {}'.format(
        'Update a user by id in the system.',
        '* Authentication required.'
    ),
    tags=['users'])
@app.route(
    f'{data.V1_STR}/users/<int:id>',
    methods=['PUT']
)
@use_kwargs({
    'email': fields.Email(required=False),
    'password': fields.String(required=False),
    'first_name': fields.String(required=False),
    'last_name': fields.String(required=False),
    'is_active': fields.Boolean(required=False)
})
@marshal_with(UserSchema())
@jwt_required
def route_users_put_by_id(
    id=None,
    email=None,
    password=None,
    first_name=None,
    last_name=None,
    is_active=None
):
    user_obj = user_provider.get_by_id(id=id)
    if user_obj is None:
        abort(400, 'The user to update doesn\'t exist in the system.')

    updated_user_obj = user_provider.update(
        user=user_obj,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        is_active=is_active
    )

    return updated_user_obj


@docs.register
@doc(
    description='{} {}'.format(
        'Delete a user by id of the system.',
        '* Authentication required.'
    ),
    tags=['users'])
@app.route(
    f'{data.V1_STR}/users/<int:id>',
    methods=['DELETE']
)
@use_kwargs({})
@marshal_with(MsgSchema())
@jwt_required
def route_users_delete_by_id(
    id=None
):
    user_obj = user_provider.get_by_id(id=id)
    if user_obj is None:
        abort(400, 'The user to delete doesn\'t exist in the system.')

    user_provider.delete(user=user_obj)

    return {'msg': 'User successfully removed from the system.'}
