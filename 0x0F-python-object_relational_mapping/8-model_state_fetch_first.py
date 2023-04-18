#!/usr/bin/python3
"""
a script that prints the first State object from the database hbtn_0e_6_usa
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
    state = session.query(State).first()
    if state:
        print("{}: {}".format(str(state.id)[0], str(state.name)))
    else:
        print("Nothing")
    # close session
    session.close()
