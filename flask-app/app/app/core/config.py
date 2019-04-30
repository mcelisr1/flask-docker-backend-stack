
# Import app code
from app.main import app
from app.core import data

# Flask variables
app.config['DEBUG'] = data.DEBUG
app.config['FLASK_DEBUG'] = data.FLASK_DEBUG
app.config['SECRET_KEY'] = data.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = data.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
