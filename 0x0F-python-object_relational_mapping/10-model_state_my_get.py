#!/usr/bin/python3

"""Script to print the State object with the
name passed as argument from the database hbtn_0e_6_usa.

Args:
    username (str): The MySQL username.
    password (str): The MySQL password.
    db_name (str): The name of the MySQL database.
    state_name (str): The name of the state to search for.

Returns:
    None

Usage:
    Run this script with four arguments:
    username, password, database name, and state name to search.
    For example: python3 script.py username password hbtn_0e_6_usa "New York"

Requirements:
    - SQLAlchemy module must be installed.
    - State and Base classes must be imported from model_state module.
    - The script connects to a MySQL server running on localhost at port 3306.
    - The state object with the provided name is printed.
    - If no state has the name searched for, "Not found" is displayed.

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
    if len(inp) < 5 or ";" in inp[4]:
        exit(1)

    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    my_query = session.query(State).filter(State.name.like(inp[4])).all()

    if len(my_query) == 0:
        print("Not found")
    else:
        print(my_query[0].id)

    session.close()
