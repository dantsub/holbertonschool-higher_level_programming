#!/usr/bin/python3
"""
Module of the class definition of a City and an instance Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'

    # identificate unique of table cities
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement="auto"
        )
    # attribute name of table cities
    name = Column(
        String(128),
        nullable=False
    )
    # foreign key for connection to state table
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
        )
