#!/usr/bin/python3

"""Script to print the first State object from the database hbtn_0e_6_usa.

Args:
    username (str): The MySQL username.
    password (str): The MySQL password.
    db_name (str): The name of the MySQL database.

Returns:
    None

Usage:
    Run this script with three arguments: username,
    password, and database name.
    For example: python3 script.py username password hbtn_0e_6_usa

Requirements:
    - SQLAlchemy module must be installed.
    - State and Base classes must be imported from model_state module.
    - The script connects to a MySQL server running on localhost at port 3306.
    - The state displayed is the first in terms of states.id.
    - The script does not fetch all states from the
    database before displaying the result.
    - If the table states is empty, prints "Nothing" followed by a new line.

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
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    object_data = session.query(State).first()
    if object_data is None:
        print("Nothing")
    else:
        print(object_data.id, object_data.name, sep=": ")
