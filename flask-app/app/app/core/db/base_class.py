# -*- coding: utf-8 -*-

# Import installed packages
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime


class CustomBase(object):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    created_at = Column(DateTime, index=True, nullable=False)


Base = declarative_base(cls=CustomBase)
