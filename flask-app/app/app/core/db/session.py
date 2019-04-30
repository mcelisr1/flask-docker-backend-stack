
# Import installed modules
from flask_sqlalchemy import SQLAlchemy

# Import app code
from app.main import app
from app.core.db.base import Base

db = SQLAlchemy(app, model_class=Base)
db_session = db.session
