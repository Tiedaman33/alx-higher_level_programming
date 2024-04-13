#!/usr/bin/python3

"""
Script to list all State objects and their corresponding
City objects from the database hbtn_0e_101_usa.

Usage:
    python script.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The username to connect to the MySQL server.
    mysql_password: The password to connect to the MySQL server.
    database_name: The name of the database to connect to.

Requirements:
    - SQLAlchemy module must be installed.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create a database engine using the provided arguments
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Retrieve all states from the database and order them by ID
    for state in session.query(State).order_by(State.id):
        # Print state ID and name
        print("{}: {}".format(state.id, state.name))

        # Iterate over the cities associated with the current state
        for city in state.cities:
            # Print city ID and name
            print("    {}: {}".format(city.id, city.name))
