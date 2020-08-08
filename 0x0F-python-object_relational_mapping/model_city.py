#!/usr/bin/python3
"""
contains the class City
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    entity city
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'))
