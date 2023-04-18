#!/usr/bin/python3
"""
a script that lists all State objects
that contain the letter a
from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # query
    state_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()
    if state_a:
        for state in state_a:
            print("{}: {}".format(str(state.id), str(state.name)))
    else:
        print("Nothing")
    # close session
    session.close()
