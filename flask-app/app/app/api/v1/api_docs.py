# Import installed packages
from apispec import APISpec
from flask_apispec import FlaskApiSpec

# Import app code
from ...main import app
from ...core import data

security_definitions = {
    'bearer': {
        'type': 'oauth2',
        'flow': 'password',
        'tokenUrl': f'{data.V1_STR}/login/access-token/',
    }
}

app.config.update({
    'APISPEC_SPEC':
    APISpec(
        title='Backend stack: API',
        version='v1',
        plugins=('apispec.ext.marshmallow', ),
        securityDefinitions=security_definitions),
    'APISPEC_SWAGGER_URL':
    f'{data.V1_STR}/swagger/'
})
docs = FlaskApiSpec(app)

security_params = [{'bearer': []}]
