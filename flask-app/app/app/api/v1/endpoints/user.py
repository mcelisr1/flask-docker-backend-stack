# -*- coding: utf-8 -*-

# Import installed packages
from flask import abort
from flask_apispec import doc, use_kwargs, marshal_with
from flask_jwt_extended import get_current_user
from flask_jwt_extended import jwt_required
from webargs import fields

# Import app code
from app.api.v1.api_docs import docs
from app.core import data
from app.main import app

# Import providers
from app.providers import user_provider

# Import required schemas
from app.schemas.msg import MsgSchema
from app.schemas.user import UserSchema


@docs.register
@doc(
    description='Create a new user with default role in the system.',
    tags=['users'])
@app.route(
    f'{data.V1_STR}/users',
    methods=['POST']
)
@use_kwargs({
    'email': fields.Email(required=True),
    'password': fields.String(required=True),
    'first_name': fields.String(required=False),
    'last_name': fields.String(required=False)
})
@marshal_with(UserSchema())
def route_users_post(
    email=None,
    password=None,
    first_name=None,
    last_name=None
):
    user_obj = user_provider.get_by_email(email=email)
    if user_obj is not None:
        abort(400, 'The email to register already exists in the system.')

    return user_provider.create(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )


@docs.register
@doc(
    description='Read existing users in the system.'
                ' * Authentication required.',
    tags=['users'])
@app.route(
    f'{data.V1_STR}/users',
    methods=['GET']
)
@marshal_with(UserSchema(many=True))
@jwt_required
def route_users_get():
    current_user = get_current_user()

    if not current_user.is_active:
        abort(403, 'Inactive user.')
    elif not user_provider.has_role_code(
        user_obj=current_user,
        role_code=data.ROLE_DEFAULT
    ):
        abort(403, "Not authorized")

    return user_provider.get_all()


@docs.register
@doc(
    description='Update a user by id in the system.'
                ' * Authentication required.',
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
    current_user = get_current_user()

    if not current_user.is_active:
        abort(403, 'Inactive user.')
    elif not current_user.is_superuser:
        abort(403, "Only a superuser can execute this action.")

    user_obj = user_provider.get_by_id(id=id)
    if user_obj is None:
        abort(400, 'The user to update doesn\'t exist in the system.')

    updated_user_obj = user_provider.update(
        user_obj=user_obj,
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
    current_user = get_current_user()

    if not current_user.is_active:
        abort(403, 'Inactive user.')
    elif not current_user.is_superuser:
        abort(403, "Only a superuser can execute this action.")

    user_obj = user_provider.get_by_id(id=id)
    if user_obj is None:
        abort(400, 'The user to delete doesn\'t exist in the system.')

    user_provider.delete(user_obj=user_obj)

    return {'msg': 'User successfully removed from the system.'}
