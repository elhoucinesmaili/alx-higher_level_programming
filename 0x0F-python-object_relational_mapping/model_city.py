#!/usr/bin/python3
"""
Defines a City class and links it to the 'cities' table in the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represents a City for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table.
        id (sqlalchemy.Column): The city's unique ID, auto-incremented.
        name (sqlalchemy.Column): The city's name.
        state_id (sqlalchemy.Column): The ID of the state the city belongs to.
    """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
