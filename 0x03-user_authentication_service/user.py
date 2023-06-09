#!/usr/bin/env python3
"""contains user model fro datbase table named
user"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR

Base = declarative_base()


class User(Base):
    """mapped class user"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(250), nullable=True)
    hashed_password = Column(VARCHAR(250), nullable=True)
    session_id = Column(VARCHAR(250), nullable=True)
    reset_token = Column(VARCHAR(250), nullable=True)
