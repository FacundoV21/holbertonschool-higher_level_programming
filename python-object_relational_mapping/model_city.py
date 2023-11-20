#!/usr/bin/python3
"""
    Create a City class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from model_state import Base


class City(Base):
    """
        Class creation
    """
    __tablename__ = "cities"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )

    name = Column(
        String(128), 
        nullable=False
    )
    
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
