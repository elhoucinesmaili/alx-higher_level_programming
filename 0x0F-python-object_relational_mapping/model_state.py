#!/usr/bin/python3
"""Lists regions"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_town import Town

Base = declarative_base()


class Region(Base):
    """Class representing the regions table"""
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    towns = relationship("Town", backref="region")
