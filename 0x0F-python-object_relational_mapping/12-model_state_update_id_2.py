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

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create a session factory
    Session = sessionmaker(bind=engine)
    # Create a session object
    session = Session()

    # Retrieve the state with ID 2 from the database
    state = session.query(State).filter_by(id=2).first()
    # Update the name of the state to "New Mexico"
    state.name = "New Mexico"
    # Commit the session to persist the changes
    session.commit()
