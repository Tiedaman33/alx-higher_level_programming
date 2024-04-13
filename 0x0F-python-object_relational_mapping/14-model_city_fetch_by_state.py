#!/usr/bin/python3
"""
Model file model_city.py containing the class definition of a City.

City class:
- Inherits from Base (imported from model_state)
- Links to the MySQL table cities
- Class attribute id represents a column of an auto-generated, unique integer, can’t be null, and is a primary key
- Class attribute name represents a column of a string of 128 characters and can’t be null
- Class attribute state_id represents a column of an integer, can’t be null, and is a foreign key to states.id
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
    # Retrieve all states from the database
    for state in session.query(State):
        # Check if the state's name contains the letter "a"
        if "a" in state.name:
            # Delete the state from the session
            session.delete(state)
    # Commit the session to persist the changes
    session.commit()
