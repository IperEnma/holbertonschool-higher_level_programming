#!/usr/bin/python3
""" prints the first State """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == '__main__':

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True, echo=False)
    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if (state):
        print("{}: {}".format(state.id, state.name))
    session.close()
