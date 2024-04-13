#!/usr/bin/python
"""
This file contains the class definition of a
State and an instance Base = declarative_base().

State class:
- Inherits from Base
- Links to the MySQL table 'states'
- Class attribute 'id' represents a column of an auto-generated,
unique integer, can't be null, and is a primary key
- Class attribute 'name' represents a column of a string
with maximum 128 characters and can't be null

Requirements:
- The script should import SQLAlchemy.
- The script should connect to a MySQL
server running on localhost at port 3306.
- WARNING: All classes that inherit from Base must be
imported before calling Base.metadata.create_all(engine).

Example usage:
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String
    from sqlalchemy import create_engine

    Base = declarative_base()

    class State(Base):
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)

    engine = create_engine('mysql://username:password@localhost:3306/database')
    Base.metadata.create_all(engine)
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
