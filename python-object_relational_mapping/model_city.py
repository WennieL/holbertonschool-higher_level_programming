#!/usr/bin/python3
"""
a python file that contains the class definition of
a City and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base

Base = declarative_base()


class City(Base):
    """
    City class representing a city entity in the database.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (int): Primary key column for the city ID.
        name (str): Column for the city name, max length 128 characters.
        state_id (int): Foreign key to the state ID from the State table.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
