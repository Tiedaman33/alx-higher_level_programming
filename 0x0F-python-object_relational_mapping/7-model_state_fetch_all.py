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

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    inp = sys.argv
    if len(inp) < 4:
        exit(1)
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    output = session.query(State).order_by(State.id).all()
    for state in output:
        print("{}: {}".format(state.id, state.name))

    session.close()
