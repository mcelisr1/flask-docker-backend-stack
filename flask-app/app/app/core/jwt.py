# Import installed modules
from flask_jwt_extended import JWTManager

# Import app code
from ..main import app
from app.core.db.session import db_session

# Import models
from app.models.user import User

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)


@jwt.user_loader_callback_loader
def get_current_user(identity):
    return db_session.query(User).filter_by(id=identity).first()
