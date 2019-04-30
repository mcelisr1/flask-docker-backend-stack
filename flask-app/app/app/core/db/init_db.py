# Import app code
from app.core import data

# Import providers
from app.providers import role_provider
from app.providers import user_provider


def load_default_data():
    role = role_provider.get_by_code(code=data.ROLE_DEFAULT)
    if role is None:
        role = role_provider.create(
            code=data.ROLE_DEFAULT,
            name='Default',
            description='General users of the system.'
        )

    user = user_provider.get_by_email(email=data.FIRST_SUPERUSER)
    if user is None:
        user = user_provider.create(
            email=data.FIRST_SUPERUSER,
            password=data.FIRST_SUPERUSER_PASSWORD,
            first_name='Super',
            last_name='User',
            is_superuser=True
        )
