#!/usr/bin/python3
""" lists all State objects from the database """

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == '__main__':

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping = True, echo = False)

    session = Session(engine)
    for state, city in session.query(State, City).filter(City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
