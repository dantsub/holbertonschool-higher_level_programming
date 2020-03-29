#!/usr/bin/python3
"""
Module of the class definition of a State and an instance Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class
    """
    __tablename__ = 'states'

    # identificate unique of table states
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement="auto"
        )
    # attribute name of table states
    name = Column(
        String(128),
        nullable=False
    )
