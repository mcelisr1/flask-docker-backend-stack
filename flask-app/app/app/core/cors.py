# Import installed packages
from flask_cors import CORS

# Import app code
from app.main import app


# Anything
CORS(app, origins='*', supports_credentials=True)
