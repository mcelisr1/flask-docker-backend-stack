# -*- coding: utf-8 -*-

# Import installed packages
from sqlalchemy import Column, String, Boolean

# Import app code
from app.core.db.base_class import Base


class User(Base):
    __tablename__ = 'user'

    # Own properties
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    is_active = Column(Boolean(), default=True, nullable=False)

    def __repr__(self):
        return f'{self.email}'
