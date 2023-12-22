#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State Class inherits from Base (declarative_base())
    
    Attributes:
        id (int): Represents a column of an auto-generated, unique integer.
        name (str): Represents a column of a string with a maximum of 128 characters.
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
