# Import app code
from app.core.db.session import db_session as DB_SESSION


db_session = DB_SESSION


def create(
    obj
):
    db_session.add(obj)
    db_session.commit()

    return obj


def get_by_id(model, id):
    return db_session.query(model).filter_by(id=id).first()


def get_all(model):
    return db_session.query(model).all()


def delete(
    obj
):
    db_session.delete(obj)
    db_session.commit()

    return True
