#!/usr/bin/python3
""" lists all State objects that contain the letter a """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == '__main__':

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1],
                argv[2],
                argv[3]
                ),
            pool_pre_ping=True,
            echo=False
            )
    session = Session(engine)

    session.query(State).filter(
            State.name.like('%a%')).delete(synchronize_session="fetch")
    session.commit()
    session.close()
