#!/usr/bin/python3
# adds the State object “Louisiana” to the database hbtn_0e_6_usa
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, pwd, data = argv[1], argv[2], argv[3]  # arguments
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, pwd, data)  # data for connection
    engine = create_engine(db, pool_pre_ping=True)  # create connection
    Base.metadata.create_all(engine)  # Initialize of linked tables
    Session = sessionmaker(bind=engine)  # Create class Session
    session = Session()  # create instance of class Session
    # new record call Louisiana
    name = "Louisiana"
    new = State(name=name)  # create a object with name="Louisiana"
    session.add(new)  # inset into table
    session.commit()  # confirm changes
    # get id new record
    id_record = session.query(State).filter_by(name=name).all()
    # print id record
    print("{}".format(id_record[0].id))
    session.close()  # close session
