# Import app code
from app.api.v1.utils.general import datetime_now
from app.core import data
from app.core.security import pwd_context

# Importing required models
from app.models.user import User

# Import providers
from app.providers import base_provider
from app.providers import role_provider


def create(
    email,
    password,
    first_name=None,
    last_name=None,
    is_active=True,
    is_superuser=False,
    role_code=data.ROLE_DEFAULT
):
    role_obj = role_provider.get_by_code(code=role_code)

    new_user_obj = User(
        created_at=datetime_now(),
        email=email,
        password=pwd_context.hash(password),
        first_name=first_name,
        last_name=last_name,
        is_active=is_active,
        is_superuser=is_superuser,
        role=role_obj
    )

    return base_provider.create(obj=new_user_obj)


def get_by_id(id):
    return base_provider.get_by_id(model=User, id=id)


def get_by_email(email):
    return base_provider.db_session.query(User).filter_by(email=email).first()


def get_all():
    return base_provider.get_all(model=User)


def update(
    user_obj,
    email=None,
    password=None,
    first_name=None,
    last_name=None,
    is_active=None,
    is_superuser=None,
    role_id=None
):
    if email:
        user_obj.email = email

    if password:
        user_obj.password = pwd_context.hash(password)

    if first_name:
        user_obj.first_name = first_name

    if last_name:
        user_obj.last_name = last_name

    if is_active is not None:
        user_obj.is_active = is_active

    if is_superuser is not None:
        user_obj.is_superuser = is_superuser

    if role_id:
        user_obj.role_id = role_id

    base_provider.db_session.commit()
    base_provider.db_session.refresh(user_obj)

    return user_obj


def delete(
    user_obj
):
    return base_provider.delete(user_obj)


def is_current_password(user_obj, password):
    correct = False
    try:
        correct = pwd_context.verify(password, user_obj.password)
    except Exception:
        print("Exception in is_current_password()")

    return correct


def has_role_code(user_obj, role_code):
    has = False
    if user_obj.role and user_obj.role.code == role_code:
        has = True

    return has
