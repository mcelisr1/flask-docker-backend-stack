# -*- coding: utf-8 -*-

# Import installed packages
from sqlalchemy import Column, String

# Import app code
from app.core.db.base_class import Base


class Role(Base):
    __tablename__ = 'role'

    # Own properties
    code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)

    # Relationships

    def __repr__(self):
        return f'{self.code} {self.name}'
