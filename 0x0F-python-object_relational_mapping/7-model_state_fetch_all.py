#!/usr/bin/python3

"""Script to retrieve and display all State
objects from the hbtn_0e_6_usa database.

Args:
    username (str): The MySQL username.
    password (str): The MySQL password.
    db_name (str): The name of the MySQL database.

Returns:
    None

Usage:
    Run this script with three arguments: username, password,
    and database name.
    For example: python3 script.py username password hbtn_0e_6_usa

Requirements:
    - SQLAlchemy module must be installed.
    - State and Base classes must be imported from model_state module.
    - The script connects to a MySQL server running on localhost at port 3306.
    - Results are sorted in ascending order by states.id.
    - Results are displayed as follows: "<state.id>: <state.name>".

Note:
    The code is not executed when imported.
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

    # Retrieve all states from the database and print their IDs and names
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
