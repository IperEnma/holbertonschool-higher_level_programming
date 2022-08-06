#!/usr/bin/python3
""" class definition of a State and an instance Base """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, BigInteger, String
from sqlalchemy import MetaData
from sqlalchemy.dialects import mysql
Base = declarative_base()


class State(Base):

    __tablename__ = 'states'
    charset = 'utf8'
    id = Column(
            mysql.INTEGER(11),
            primary_key=True,
            autoincrement=True,
            nullable=False,
            unique=True
            )
    name = Column(String(128), nullable=False)
    __table_args__ = {'mysql_charset ': ' latin1 '}
