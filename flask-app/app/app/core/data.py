# -*- coding: utf-8 -*-

import os
from datetime import timedelta


ACCESS_TOKEN_EXPIRE_MINUTES = timedelta(
    minutes=60
)
DATA_ROOT_PATH = '/app-data'
DEBUG = True
ENV = os.getenv("ENV")
FLASK_DEBUG = 1
POSTGRES_DB = 'app'
POSTGRES_PASSWORD = 'JpELH7HYnPnYjsz5'
POSTGRES_SERVER = 'db'
POSTGRES_USER = 'admin'
REFRESH_TOKEN_EXPIRE_MINUTES = timedelta(
    minutes=90
)
SECRET_KEY = 'B9yggMGjj54D6nLrgdb9TgyP'
SQLALCHEMY_DATABASE_URI = (
    'postgresql://{}:{}@{}/{}'.format(
        POSTGRES_USER,
        POSTGRES_PASSWORD,
        POSTGRES_SERVER,
        POSTGRES_DB
    )
)
V1_STR = "/v1"

if ENV == 'prod':
    DEBUG = False
    FLASK_DEBUG = 0

# Create data directories
if not os.path.exists(DATA_ROOT_PATH):
    os.makedirs(DATA_ROOT_PATH)
