#!/usr/bin/python3
'''
a script that prints all City objects from the database
'''

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import Base, State

if __name__ == "__main__":
    # create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # wquey all State objects, and order by id
    for city, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # close session
    session.close()
