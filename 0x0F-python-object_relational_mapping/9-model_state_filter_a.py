#!/usr/bin/python3
"""Script to list all State objects that
contain the letter 'a' from the database hbtn_0e_6_usa.

Args:
    username (str): The MySQL username.
    password (str): The MySQL password.
    db_name (str): The name of the MySQL database.

Returns:
    None

Usage:
    Run this script with three
    arguments: username, password, and database name.
    For example: python3 script.py username password hbtn_0e_6_usa

Requirements:
    - SQLAlchemy module must be installed.
    - State and Base classes must be imported from model_state module.
    - The script connects to a MySQL server running on localhost at port 3306.
    - Results are sorted in ascending order by states.id.
    - Only State objects containing the letter 'a' are included in the results.
    - The results are displayed in the format: "<state.id>: <state.name>".

Note:
    The code is not executed when imported.
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")
