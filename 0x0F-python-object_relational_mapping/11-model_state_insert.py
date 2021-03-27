#!/usr/bin/python3
'''Module with script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa'''

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

    la = State(name='Louisiana')
    session.add(la)
    session.commit()
    print(la.id)

    session.close()
