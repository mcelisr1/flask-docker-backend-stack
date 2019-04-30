
# Import app code
from app.main import app  # noqa
# Set up global variables
from app.core import data  # noqa
# Set up Config Environments
from app.core import config  # noqa
# Set up flask db session
from app.core.db.session import db_session  # noqa

# Load dafault data on DB
from app.core.db.init_db import load_default_data

# Set up CORS
from . import cors  # noqa

from .jwt import jwt  # noqa
from . import errors  # noqa

# Set up Flask Endpoints
from ..api.v1 import api as api_v1  # noqa


@app.before_first_request
def setup():
    # Load dafault data on DB
    load_default_data()
