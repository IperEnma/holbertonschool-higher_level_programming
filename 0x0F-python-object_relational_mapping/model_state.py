#!/usr/bin/python3
""" class definition of a State and an instance Base """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects import mysql

Base = declarative_base()


class State(Base):
    """ ORM MAPPING """
    __tablename__ = 'states'
    id = Column(
            mysql.INTEGER(11),
            primary_key=True,
            autoincrement=True,
            nullable=False,
            unique=True
            )
    name = Column(String(128), nullable=False)
    __table_args__ = {'mysql_charset ': ' latin1 '}
