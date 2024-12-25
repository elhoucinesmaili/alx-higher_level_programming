#!/usr/bin/python3
"""Defines the State class for the states table"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class State(Base):
    """Class representing the 'states' table in the database"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

    # Relationship between State and City (one-to-many)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",   # Automatically delete cities when state is deleted
        backref=backref("state", cascade="all"),  # Allows access to state from city
        single_parent=True  # Ensures only one parent for each city
    )
