#!/usr/bin/python3
# prints the State object with the name passed as
# argument from the database hbtn_0e_6_usa
from sys import argv
from model_state import Base, State
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

    records = session.query(State).filter_by(name=name).all()  # save records
    # print records
    if records:
        [print("{}".format(state.id)) for state in records]
    else:
        print("Not found")
    session.close()  # close session
