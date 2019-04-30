
# Import installed packages
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token

# Import app code
from app.core import data


def generate_tokens(identity, token_type='Bearer'):
    access_token = create_access_token(
        identity=identity,
        expires_delta=data.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    refresh_token = create_refresh_token(
        identity=identity,
        expires_delta=data.REFRESH_TOKEN_EXPIRE_MINUTES
    )

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'token_type': token_type
    }
