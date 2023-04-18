#!/usr/bin/python3
'''
a script that adds the State object “Louisiana” to the database
'''

from sys import argv
from sqlalchemy import create_engine
from sqlacademy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # create new state
    new_state = State(name="Louisiana")
    # add new state to session
    session.add(new_state)
    # commit changes
    session.commit()
    # print id of new state
    print(new_state.id)
    # close session
    session.close()
