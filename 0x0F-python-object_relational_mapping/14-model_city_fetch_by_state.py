#!/usr/bin/python3
# prints all City objects from the database hbtn_0e_14_usa
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, pwd, data, name = argv[1], argv[2], argv[3], argv[4]  # arguments
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, pwd, data)  # data for connection
    engine = create_engine(db, pool_pre_ping=True)  # create connection
    Base.metadata.create_all(engine)  # Initialize of linked tables
    Session = sessionmaker(bind=engine)  # Create class Session
    session = Session()  # create instance of class Session
    # get data
    rd = session.query(State, City).filter(State.id == City.state_id)
    # print records
    [print("{}: ({}) {}".format(r[0].name, r[1].id, r[1].name)) for r in rd]
    session.close()  # close session
