#!/usr/bin/python3
'''Module with script that lists all State objects
 from the database hbtn_0e_6_usa)'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

vroom = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    engine = create_engine(vroom)

    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).order_by(State.id).first()

    if instance:
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")
    session.close()
