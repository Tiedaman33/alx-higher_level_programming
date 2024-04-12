#!/usr/bin/python

from sqlalchemy import Column, Integer, String, Metadata
from sqlalchemy.ext..declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """
    class with attributes if state
    """
    __tablename__ = 'states'
    id = column(Integer, unique=True, nullable=False, primary_key=True)
    name = column(String(128), nullable=False)

