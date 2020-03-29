#!/usr/bin/python3
# deletes all State objects with a name containing the
# letter a from the database hbtn_0e_6_usa
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

if __name__ == "__main__":
    user, pwd, data = argv[1], argv[2], argv[3]  # arguments
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, pwd, data)  # data for connection
    engine = create_engine(db, pool_pre_ping=True)  # create connection
    Base.metadata.create_all(engine)  # Initialize of linked tables
    Session = sessionmaker(bind=engine)  # Create class Session
    session = Session()  # create instance of class Session
    # get id
    _fr = State.name.like(func.binary('%a%'))
    # delete records
    session.query(State).filter(_fr).delete(synchronize_session='fetch')
    session.commit()  # confirm changes
    session.close()  # close session
