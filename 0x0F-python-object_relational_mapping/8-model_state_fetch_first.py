#!/usr/bin/python3
# prints the first State object from the database hbtn_0e_6_usa
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, pwd, data = argv[3], argv[2], argv[1]  # arguments
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, pwd, data)  # data for connection
    engine = create_engine(db, pool_pre_ping=True)  # create connection
    Base.metadata.create_all(engine)  # Initialize of linked tables
    Session = sessionmaker(bind=engine)  # Create class Session
    session = Session()  # create instance of class Session
    # save first record
    record = session.query(State).order_by(State.id).first()
    if record:
        print("{}: {}".format(record.id, record.name))
    else:
        print("Nothing")
    session.close()  # close session
