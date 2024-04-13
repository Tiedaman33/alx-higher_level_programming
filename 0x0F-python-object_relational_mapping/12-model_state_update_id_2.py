#!/usr/bin/python3
"""
Script to change the name of a State object in the database hbtn_0e_6_usa.

Usage:
    python script.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The username to connect to the MySQL server.
    mysql_password: The password to connect to the MySQL server.
    database_name: The name of the database to connect to.

Requirements:
    - SQLAlchemy module must be installed.
    - State and Base classes must be imported from model_state module.
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    new_instance = session.query(State).fiter_by(id=2).first()
    new_instance.name = 'New Mexico'
    session.commit()
