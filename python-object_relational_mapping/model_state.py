#!/usr/bin/python3
"""
a python file that contains the class definition of
a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class representing a state entity in the database.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (int): Primary key column for the state ID.
        name (str): Column for the state name, max length 128 characters.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
