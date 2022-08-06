#!/usr/bin/python3
""" class definition of a State and an instance Base """


from sqlalchemy import ForeignKey, Column, BigInteger, String
from sqlalchemy import MetaData
from sqlalchemy.dialects import mysql
from model_state import Base


class City(Base):

    __tablename__ = 'cities'
    charset = 'utf8'
    id = Column(
            mysql.INTEGER(11),
            primary_key=True,
            autoincrement=True,
            nullable=False,
            unique=True
            )
    name = Column(String(128), nullable=False)
    state_id = Column(
            mysql.INTEGER(11),
            ForeignKey("state.id"),
            nullable=False
            )
    __table_args__ = {'mysql_charset ': ' latin1 '}
