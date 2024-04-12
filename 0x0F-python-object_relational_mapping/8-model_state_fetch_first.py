#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    object_data = session.query(State).first()
    if object_data is None:
        print("Nothing")
    else:
        print(object_data.id, object_data.name, sep=": ")