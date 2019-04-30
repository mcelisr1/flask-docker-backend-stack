# Import installed modules
from flask import abort
from flask_apispec import doc, use_kwargs, marshal_with
from flask_jwt_extended import get_current_user
from flask_jwt_extended import jwt_refresh_token_required
from webargs import fields

# Import app code
from app.api.v1.api_docs import docs
from app.core import data
from app.main import app

# Import providers
from app.providers import token_provider
from app.providers import user_provider

# Import required schemas
from app.schemas.token import TokenSchema


@docs.register
@doc(
    description='OAuth2 compatible token login,'
                ' get an access token for future requests.',
    tags=['login'])
@app.route(
    f'{data.V1_STR}/login/access-token',
    methods=['POST']
)
@use_kwargs({
    'email': fields.Email(required=True),
    'password': fields.Str(required=True)
    })
@marshal_with(TokenSchema())
def route_login_access_token_post(
    email,
    password
):
    user_obj = user_provider.get_by_email(email=email)
    if user_obj is None:
        abort(400, 'The email doesn\'t exist in the system.')

    correct_password = user_provider.is_current_password(user_obj, password)
    if not correct_password:
        abort(400, 'Incorrect password.')

    if not user_obj.is_active:
        abort(400, 'The user is inactive in the system.')

    return token_provider.generate_tokens(user_obj.id)


@docs.register
@doc(
    description='OAuth2 compatible token login,'
                ' get a new access token with a given refresh-token',
    tags=['login'])
@app.route(
    f'{data.V1_STR}/login/refresh-token',
    methods=['POST']
)
@marshal_with(TokenSchema())
@jwt_refresh_token_required
def route_login_refresh_token_post():
    current_user = get_current_user()

    return token_provider.generate_tokens(current_user.id)
