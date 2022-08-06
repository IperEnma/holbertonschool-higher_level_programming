#!/usr/bin/python3
""" class definition of a State and an instance Base """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String

Base = declarative_base()


class State(Base):
    """ ORM MAPPING """
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            autoincrement="auto",
            nullable=False,
            unique=True
            )
    name = Column(String(128), nullable=False)
    __table_args__ = {'mysql_charset ': ' latin1 '}
