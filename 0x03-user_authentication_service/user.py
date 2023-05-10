#!/usr/bin/env python3
"""
User SQL
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

Class User(Base):
    """
    Represents a record from the `user` table.
    """
    __table__= "users"
    id = Column(Interger, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String,(250), nullable=False)
    session_id = Column (String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)


