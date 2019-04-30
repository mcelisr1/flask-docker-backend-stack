# Import app code
from app.core.db.session import db_session
from app.core.security import pwd_context

# Importing required models
from app.models.user import User


def get_by_id(id):
    return db_session.query(User).filter_by(id=id).first()


def get_by_email(email):
    return db_session.query(User).filter_by(email=email).first()


def get_all():
    return db_session.query(User).all()


def update(
    user,
    email=None,
    password=None,
    first_name=None,
    last_name=None,
    is_active=None
):
    if email:
        user.email = email

    if password:
        user.password = pwd_context.hash(password)    

    if first_name:
        user.first_name = first_name

    if last_name:
        user.last_name = last_name

    if is_active is not None:
        user.is_active = is_active

    db_session.commit()
    db_session.refresh(user)

    return user


def delete(
    user
):
    db_session.delete(user)
    db_session.commit()

    return True


def is_current_password(user, password):
    correct = False
    try:
        correct = pwd_context.verify(password, user.password)
    except Exception:
        print("Exception in is_current_password()")

    return correct


def is_active(user):
    return user.is_active
