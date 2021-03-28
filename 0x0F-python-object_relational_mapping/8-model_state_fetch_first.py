#!/usr/bin/python3
'''Module with script that lists all State objects
 from the database hbtn_0e_6_usa)'''

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    vroom = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(argv[1], argv[2], argv[3])
    engine = create_engine(vroom)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).order_by(State.id).first()

    try:
        print("{}: {}".format(instance.id, instance.name))
    except BaseException:
        print("Nothing")
    session.close()
