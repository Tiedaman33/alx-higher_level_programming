#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):

    """
    City Base class
    """
    __table__name = 'cities'
    id = column(Integer, unique=True, nullables=False)
    state_id = column(Integer, ForeignKey("states.id"), nullable=False)
