#!/usr/bin/python3
'''
a script that chaanges the name of a state object from the database
'''
from sys import argv
from mysqlacademy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # create the session
    Session = sessionmaker(bind=engine)
    session = Session()
    # query the database
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
