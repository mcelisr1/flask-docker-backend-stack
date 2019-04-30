# -*- coding: utf-8 -*-

# Import installed packages
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

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
    is_superuser = Column(Boolean(), default=False, nullable=False)

    # Relationships
    role_id = Column(
        Integer,
        ForeignKey('role.id'),
        index=True,
        nullable=False
    )
    role = relationship('Role', foreign_keys=[role_id])

    def __repr__(self):
        return f'{self.email}'
