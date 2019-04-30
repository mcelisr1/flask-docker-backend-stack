# Import app code
from app.api.v1.utils.general import datetime_now

# Importing required models
from app.models.role import Role

# Import providers
from app.providers import base_provider


def create(
    code,
    name,
    description=None
):
    new_role_obj = Role(
        created_at=datetime_now(),
        code=code,
        name=name,
        description=description
    )

    return base_provider.create(obj=new_role_obj)


def get_by_id(id):
    return base_provider.get_by_id(model=Role, id=id)


def get_by_code(code):
    return base_provider.db_session.query(Role).filter_by(code=code).first()


def get_all():
    return base_provider.get_all(model=Role)


def update(
    role_obj,
    code=None,
    name=None,
    description=None
):
    if code:
        role_obj.code = code

    if name:
        role_obj.name = name

    if description:
        role_obj.description = description

    base_provider.db_session.commit()
    base_provider.db_session.refresh(role_obj)

    return role_obj


def delete(
    role_obj
):
    return base_provider.delete(role_obj)
