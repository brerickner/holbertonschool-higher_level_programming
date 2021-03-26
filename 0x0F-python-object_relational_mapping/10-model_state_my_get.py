#!/usr/bin/python3
'''script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa'''

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

vroom = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    engine = create_engine(vroom)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    stateMatch = session.query(State).order_by(
        State.id).filter(State.name == argv[4])
    try:
        print("{}".format(stateMatch.id))
    except BaseException:
        print("Not Found")
    session.close()
