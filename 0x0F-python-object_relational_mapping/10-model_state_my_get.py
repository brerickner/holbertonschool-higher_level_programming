#!/usr/bin/python3
'''script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa'''

from sys import argv
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    vroom = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(vroom)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    stateMatch = session.query(State).order_by(
        State.id).filter(State.name == argv[4])
    try:
        print(stateMatch.id)
    except:
        print("Not Found")
    session.close()
